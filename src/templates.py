from src.output import Output


def base_report(output: Output, owner, commit_url, head_sha):
    workspace_url = f"http://test.ikido.tech:8085/#/workspace/{output.workspace_id}"
    return f'''## [IKIDO]({workspace_url}) Report
> The <a href="{commit_url}" title="@{owner}">{head_sha[:6]}</a> (@{owner}) scan result:
* **Total Found:** {output.total_count}
* :heavy_check_mark: **OK** {output.ok_count}
* :small_orange_diamond: **Low Risk** {output.low_count}
* :large_orange_diamond: **Medium Risk** {output.medium_count}
* :red_circle: **High Risk** {output.high_count}
* :white_square_button: **Not Found** {output.not_found_count}

For more information please visit [IKIDO]({workspace_url}) website'''


def risk_table_report(output: Output, risk='high'):
    titles = ('Customer PN', 'Manufacturer PN', 'Life Cycle', 'Risk Reason', 'Category', 'Item description')
    report_begin = '## High Risk items details\n'
    header_line = f'| {" | ".join(titles)} |\n'
    header_template_line = '| ----- ' * len(titles) + '|\n'
    report = report_begin + header_line + header_template_line
    items = getattr(output, risk)
    for item in items:
        try:
            item_list = [
                item['item_sku'],
                item['manufacturer_sku'],
                item['life_cycle'],
                item['risk_reason'],
                item['item_category'],
                item['item_name']
            ]
            report += f"| {' | '.join(item_list) } |\n"
        except Exception as ex:
            raise Exception(f'Failed to add item to table'
                            f'Item: {item}'
                            f'Exception: {ex}')
    return report


def check_output(title, summary, text):
    return {
                "title": title,
                "summary": summary,
                "text": text
            }

