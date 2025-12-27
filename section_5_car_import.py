from blueprint.section_5_custom_class import Car

bmw = Car(
    color = "Pink",
    engine_type = "Roket"
)

bmw.start_engine()
print(vars(bmw))

bmw.speed_up(6)
print(vars(bmw))

for i in range(1, 21):
    bmw.speed_up(20)
    print(vars(bmw)["speed"])
for i in range(1, 21):
    bmw.speed_down(20)
    print(vars(bmw)["speed"])