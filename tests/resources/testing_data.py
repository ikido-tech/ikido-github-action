import os


class Data:
    def __init__(self):
        self.path = os.path.abspath(__file__.rsplit('/', 1)[0])
        self.item_1_path = f'{self.path}/AS0A823-H8SB-7H.json'
        self.item_2_path = f'{self.path}/C1005X7R1E104M.json'
        self.item_3_path = f'{self.path}/RC0402JR-0739RL.json'
        self.output_risk_3 = f'{self.path}/output_risk_3.txt'
        self.insights_risk_3 = f'{self.path}/insights_risk_3.csv'
        self.output_risk_2 = f'{self.path}/output_risk_2.txt'
        self.insights_risk_2 = f'{self.path}/insights_risk_2.csv'
        self.output_risk_1 = f'{self.path}/output_risk_1.txt'
        self.insights_risk_1 = f'{self.path}/insights_risk_1.csv'
        self.output_risk_0 = f'{self.path}/output_risk_0.txt'
        self.insights_risk_0 = f'{self.path}/insights_risk_0.csv'
        self.base_report = f'{self.path}/base_report.txt'
        self.risk_table_report = f'{self.path}/risk_table_report.txt'
