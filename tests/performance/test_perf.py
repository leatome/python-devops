def test_perf(benchmark):
    data = list(range(1000))
    benchmark(sum, data)
