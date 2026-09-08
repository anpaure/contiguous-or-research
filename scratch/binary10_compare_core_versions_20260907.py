"""Check that a refactored generator preserves all 60 canonical literal cores."""
import importlib.util
import os
import sys

modules = []
for index, path in enumerate(sys.argv[1:]):
    spec = importlib.util.spec_from_file_location(f"core{index}",path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    modules.append(module)
assert len(modules) == 2
os.environ["BINARY10_CORE_FIRST_ORDER"] = "regular"
os.environ["BINARY10_LAST_VARIANT"] = "0"
lower, matchings = modules[0].all_fixed_matchings()
assert (lower, matchings) == modules[1].all_fixed_matchings()
for upper in matchings:
    assert modules[0].build_core(lower,upper) == modules[1].build_core(lower,upper)
print("PASS exact preservation of all 60 canonical literal cores")
