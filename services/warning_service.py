class WarningService:
    @staticmethod
    def get_warning_statistics():
        return {
            "totalWarnings": 223,
            "realWarnings": 95,
            "falseWarnings": 30,
            "warningVideoSegments": 78,
            "videoSegments": 345,
            "arcChartData": [
                {"label": "总告警", "value": 123},
                {"label": "真实告警", "value": 95},
                {"label": "误报", "value": 28},
                {"label": "视频段数", "value": 10}
            ],
            "warningTypeData": [
                {"label": "类型1", "value": 40},
                {"label": "类型2", "value": 25},
                {"label": "类型3", "value": 15},
                {"label": "类型4", "value": 10},
                {"label": "类型5", "value": 5},
                {"label": "类型6", "value": 5}
            ],
            "monthData": [
                {"category": "1月", "value": 20},
                {"category": "2月", "value": 30},
                {"category": "3月", "value": 25},
                {"category": "4月", "value": 40},
                {"category": "5月", "value": 35},
                {"category": "6月", "value": 15},
                {"category": "7月", "value": 27},
                {"category": "8月", "value": 55},
                {"category": "9月", "value": 5}
            ],
            "yearData": [
                {"category": "2020", "value": 50},
                {"category": "2021", "value": 60},
                {"category": "2022", "value": 70},
                {"category": "2023", "value": 55},
                {"category": "2024", "value": 35},
                {"category": "2025", "value": 80}
            ]
        }
