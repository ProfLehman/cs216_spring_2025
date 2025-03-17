# Animal Class
```mermaid
classDiagram
    class Animal {
        - string animal_type
        - string name
        - string sound
        + Animal(string animal_type, string name, string sound)
        + string get_animal_type()
        + void set_animal_type(string animal_type)
        + string get_name()
        + void set_name(string name)
        + string get_sound()
        + void set_sound(string sound)
        + void speak()
        + string __str__()
    }
