# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from datadog_checks.dotnetclr import DotnetclrCheck


def test_cache(benchmark):
    instance = {
        'cache_counter_instances': True,
        'host': '.',
    }
    check = DotnetclrCheck('dotnetclr', {}, {}, [instance])

    # Run once to get any PDH setup out of the way.
    check.check(instance)

    benchmark(check.check, instance)


def test_no_cache(benchmark):
    instance = {
        'cache_counter_instances': False,
        'host': '.',
    }
    check = DotnetclrCheck('dotnetclr', {}, {}, [instance])

    # Run once to get any PDH setup out of the way.
    check.check(instance)

    benchmark(check.check, instance)
