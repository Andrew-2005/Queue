import subprocess
import sys
from pathlib import Path


TASK_FILES = (
    "task1_first_unique_char.py",
    "task2_stack_using_queues.py",
    "task3_recent_counter.py",
    "task4_circular_deque.py",
    "task5_circular_queue.py",
    "task6_stamping_sequence.py",
    "task7_sliding_window_max.py",
    "task8_constrained_subsequence_sum.py",
)


# Запускає кожну задачу окремо й повертає код помилки, якщо є збій.
def main():
    project_dir = Path(__file__).resolve().parent
    failed = False
    for filename in TASK_FILES:
        result = subprocess.run(
            [sys.executable, "-E", "-B", str(project_dir / filename)],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0 and result.stdout.strip() == "OK":
            print(f"{filename}: OK")
        else:
            print(f"{filename}: FAIL")
            for output in (result.stdout, result.stderr):
                if output:
                    print(output.rstrip())
            failed = True
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
