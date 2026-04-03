import random
from datetime import datetime, timezone


def measure_temperature_mock(seed: int | None = None) -> float:
    """Mock の体温を生成する．"""
    random.seed(seed)
    return round(random.uniform(35.8, 40.0), 1)


def main() -> None:
    # 実行時刻を残しておくと，定期実行時のトレースがしやすい．
    measured_at = datetime.now(timezone.utc).isoformat()
    temperature = measure_temperature_mock()
    print(f"[{measured_at}] Mock temperature: {temperature}℃")


if __name__ == "__main__":
    main()
