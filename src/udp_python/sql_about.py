from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:example@localhost:15001/iot", echo=True)
print(engine.execute("select 1").scalar)

# class CustomSingleton(type):
#     _instance = {}
#     def __call__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super(CustomSingleton, cls).__call__(*args, **kwargs)
#         else:
#             cls._instance.__init__(*args, **kwargs)

#         return cls._instance

