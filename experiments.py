import mlflow
def calculator(a,b,opration=None):
    if opration =="add":
        return (a+b)
    if opration =="mult":
        return (a*b)
    if opration =="sub":
        return (a-b)
    if opration =="div":
        return (a/b)
if __name__ == "__main__":
    with mlflow.start_run():
        a,b,opt = 20,40, "div"
        result = calculator(a,b,opt)
        mlflow.log_param('a',a)
        mlflow.log_param('b',b)
        mlflow.log_param('opt',opt)
        print(f"the result is {result}")
        mlflow.log_param("Result",result)

