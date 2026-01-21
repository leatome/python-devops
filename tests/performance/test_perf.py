from app.utils import doThing

def test_do_thing_perf(benchmark):
    benchmark(doThing, "perf", 1,2,3,4,5,6,7,8,9)
