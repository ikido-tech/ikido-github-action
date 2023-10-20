import re
import logging

ITEM_STAT_REGEX = re.compile(r'NOT_FOUND=(\d+), OK=(\d+), LOW=(\d+), MEDIUM=(\d+), HIGH=(\d+)')
logger = logging.getLogger(__name__)


class Output:
    def __init__(self, output_path, insights_path):
        self.output_path = output_path
        self.insights_path = insights_path
        self.not_found_count = 0
        self.ok_count = 0
        self.low_count = 0
        self.medium_count = 0
        self.high_count = 0
        self.workspace_id = ''
        self.insights: list[dict] = []
        self.not_found: list[dict] = []
        self.ok: list[dict] = []
        self.low: list[dict] = []
        self.medium: list[dict] = []
        self.high: list[dict] = []
        self.parse_output()
        self.parse_insights()
        self.total_count = self.ok_count + self.low_count + self.medium_count + self.high_count + self.not_found_count

    def parse_output(self):
        with (open(self.output_path, 'r', encoding='utf-8') as file):
            output = file.readlines()
            for line in output:
                if 'ID=' in line:
                    self.workspace_id = line.split('ID=')[1].strip()
                elif 'Summary: ' in line:
                    not_found_count, ok_count, low_count, medium_count, high_count = \
                        ITEM_STAT_REGEX.findall(line)[0]
                    self.not_found_count, self.ok_count, self.low_count, self.medium_count, self.high_count = \
                        int(not_found_count), int(ok_count), int(low_count), int(medium_count), int(high_count)
                    break

    def parse_insights(self):
        with open(self.insights_path, 'r', encoding='utf-8') as file:
            content_headers = [header.strip('"') for header in file.readline().split(',')]
            insights = file.readlines()
            for line in insights:
                try:
                    records = line.strip('"').split('","')
                    row_dict = {header: record for header, record in zip(content_headers, records)}
                    life_cycle = 'Active'
                    if 'eol_indication' in row_dict and row_dict['eol_indication'] == 'True':
                        life_cycle = 'EOL'
                    elif 'nrfnd_indication' in row_dict and row_dict['nrfnd_indication'] == 'True':
                        life_cycle = 'NRFND'
                    row_dict['life_cycle'] = life_cycle
                    row_dict['risk_reason'] = row_dict['insight_warning'].replace('_', ' ').capitalize()
                    self.insights.append(row_dict)
                    if row_dict['risk'] == '0':
                        self.ok.append(row_dict)
                    elif row_dict['risk'] == '1':
                        self.low.append(row_dict)
                    elif row_dict['risk'] == '2':
                        self.medium.append(row_dict)
                    elif row_dict['risk'] == '-1':
                        self.not_found.append(row_dict)
                    elif row_dict['risk'] == '3':
                        self.high.append(row_dict)
                except Exception as ex:
                    logger.warning(f'Failed to parse line\n'
                                   f'Line: {line}'
                                   f'Exception: {ex}')
