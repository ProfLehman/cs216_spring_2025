# Student Class
```mermaid
classDiagram
    class Student {
        - string name
        - int age
        - string major
        + Student(name="unknown", age=-1, major="undeclared")
        + set_name(new_name: string): void
        + set_age(new_age: int): void
        + set_major(new_major: string): void
        + get_name(): string
        + get_age(): int
        + get_major(): string
        + canVote(): bool
        + display(): void
        + __str__(): string
    }
