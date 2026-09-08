# Generic exact-SAT containment-cap regression

## Scope

`exact_or_sat.cpp` now uses the simultaneous containment-multiplicity cap

\[
c_s(n)=\min_r\left(n-\binom{k}{r}
 +\mathbf 1_{r\le s}\binom{s}{r}\right)
\]

over ranks with `C(k,r)<=n`.  The mathematical proof and specialized
`k=11` audit are in `CONTAINMENT_MULTIPLICITY_INDEPENDENT_AUDIT.md`.

Source SHA-256:

```text
c1832b235f75be91066fc454ac7c6c46d29610a22aa2826d34c404915600f550
```

## Remote compilation and exact small regression

The source was copied to the remote Linux host and compiled with GCC `-O3`
and `-march=native`; no production solve was run on the local Mac.  The
following exact instance was generated and solved with Kissat:

```text
k=4, n=7
variables=845 clauses=2772
s SATISFIABLE
```

Decoding through the same generator produced

```text
5 9 1 2 4 8 10
```

An independent suffix-OR verifier then reported

```text
length=7 covered=15/15 missing=0
```

Relevant remote artifact hashes were:

```text
bf06e898ee28206bc7b443839869e28fd3283dc62983eef14270f1bd17dcae31  k4n7.cnf
276c559b62237d2581864f5b2c49df1554846d9001874cb6d1fed9c08c065b4a  k4n7.model
9af05674ee4aa0c73bbe18f46d96deca0576a632d375409470745caa2a7107a9  array.txt
```

This regression verifies executable generation, solving, decoding, and
independent coverage on a known optimum.  It is not a proof of any unresolved
larger instance; the containment theorem supplies the logical validity of the
new pruning.
