# Independent audit of the Type-I suffix-core subcube circuit

## Verdict

**PASS.**  Under the conjunction of the existing Type-I and exact-subcube
guards, the source soundly and completely encodes

\[
 7a_{28}^C+5a_{29}^C+3a_{30}^C+a_{31}^C\le461.
\]

The incremental circuit has exactly **25 variables and 189 clauses**.  No
variable or clause is added to Type II or to a build with the subcube guard
absent.

## 1. Mathematical branch identity

The separately audited Type-I branch fixes `A[0]=63` and forbids every other
literal rank-six entry.  The suffix `1,...,464` is the rank-at-most-five core.
For a six-set `U`, the removed endpoint belongs to the support of `U` exactly
when `U=63`.  Hence the production reuse

```text
p_U^C=p_U          (U != 63)
p_63^C=p_63-1
```

is exact.

## 2. Charge algebra

Independent evaluation of the exact `d=3` run-capacity envelope gives

```text
eta(28,29,30,31,>=32) = 7,5,3,1,0.
```

The core support theorem forces `p_63^C>=28`, so the added comparator
`p_63>=29` is necessary and valid.  On that range,

```text
eta(p_63-1)-gamma(p_63)
  = 2*(p_63<=31) + (p_63==32).
```

The source's existing `endpoint_low31` flag is an equivalence.  The new
`eq32` clauses are also an equivalence: they require bit five true and every
other bit of the nine-bit population count false.  The correction is then
added by exact full adders, including the final carry, before a direct
first-difference comparison to 461.  There is no modular truncation.

## 3. Independent exhaustive checker

`scratch/verify_k11_type1_core_subcube_encoding.py` does not include or call
the production circuit.  It verifies:

* all 1,024 assignments of the nine count bits and `eq32` output;
* the `eta` table from the closed run-capacity formula;
* the correction identity for all `29<=p_63<=465`;
* equivalence of the encoded and theorem inequalities for every possible
  aggregate charge from the other 461 subcubes;
* the production wiring anchors;
* the exact `25 / 189` inventory.

Its output is

```text
p_63=32 equivalence gate: PASS
eta(p_63-1)=gamma(p_63)+delta truth table: PASS
adjusted <=461 comparator semantics: PASS
Type-I core inventory: 25 variables, 189 clauses: PASS
production wiring anchors: PASS
```

## 4. Build regressions

The production source compiles cleanly against the build-only CaDiCaL test
double.  With the full exact Type-I guard set, the reported inventory is

```text
variables=3633121 clauses=19448586
subcube_deficiency_variables=646806
subcube_deficiency_clauses=4309599
subcube_type1_core_variables=25
subcube_type1_core_clauses=189.
```

The same source under Type II leaves the subcube module at its prior frozen
values

```text
subcube_deficiency_variables=646781
subcube_deficiency_clauses=4309410
subcube_type1_core_variables=0
subcube_type1_core_clauses=0.
```

The current whole Type-II build is `3640328 / 19476694`; its difference from
the older whole-build inventory comes solely from a separately audited
Type-II component/pin module, not from this Type-I core edit.

The all-off absent and explicit-zero subcube guards both produce

```text
CLAUSE_STREAM_FNV64=ad22e261832b9ae2 ADD_CALLS=55261249.
```

The hash stub is only a deterministic build auditor, never a SAT solver.

The final combined-source and checker hashes are

```text
1c3ce629c74aeef7339e2d43bd2f922aaf5b98d24f6a993d2d4f01aea7c63d06
  k11_forest_sat.cpp
d06bcd3f740b0c1d5878a13391c29302d5007f4b1b181f039f5c96c945c49c6d
  scratch/verify_k11_type1_core_subcube_encoding.py
```

## 5. Evidentiary scope

This audit establishes circuit exactness and guard isolation.  It establishes
neither satisfiability nor unsatisfiability of the 465-entry formula.  Search
results require the same model/proof verification standards as the parent
forest encoding.
