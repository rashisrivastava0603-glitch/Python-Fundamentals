def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_kwargs(name="Rashi",Occupation="Software Engineer",Specialization="AI/ML")
print_kwargs(name="Akshat",Occupation="Chemical Engineer") 
print_kwargs(name="Rubi",Occupation="Civil Engineer")
print_kwargs(name="Jatin",Occupation="Machenical Engineer")
print_kwargs(name="Vansh",Occupation="Software Engineer")
