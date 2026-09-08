# A residence-clean interior rethread of the repaired `m=5` Catalan forest

Date: 2026-07-31  
Status: exact finite theorem with independent literal replay; no all-`m`
rethread theorem and no completed connector/compiler

## 0. Verdict

The 31 immutable depth-two residence defects in the synchronized repaired
`m=5` Catalan forest are not intrinsic to its exact two palettes.  There is
another perfect rank-4/rank-6 diamond matching whose Johnson lift is a
spanning 42-path forest and has **no internal coordinate run of length one or
two**.

The new forest is obtained in the palette-preserving exchange space generated
by alternating `C4/C6` diamond circuits.  The final certificate is a literal
matching, so its validity does not depend on the stochastic search history.

This closes residence on path interiors only.  The new path endpoints still
have short boundary runs, and its internal fragments miss 21 deeper-shadow
targets.  A residence-compatible, flag-complete socket chronology and the
lower compiler remain open.

## 1. Exact certificate

Let

\[
 {\cal L}={ [10]\choose4},\qquad {\cal U}={ [10]\choose6}.
\]

The certificate lists a bijection

\[
                    \sigma:{\cal L}\longrightarrow{\cal U}
\]

with `L subset sigma(L)` for every `L`.  Lift the diamond `(L,sigma(L))` to
the Johnson edge joining the two rank-five sets strictly between `L` and
`sigma(L)`.

### Theorem 1.1

The 210 lifted edges have the following properties.

1. Their lower intersections are all 210 rank-four sets, once each.
2. Their upper unions are all 210 rank-six sets, once each.
3. They form a spanning forest on all 252 rank-five sets, with exactly 42
   path components.
4. Along every path, every positive coordinate run bounded strictly inside
   that path has length at least three.

Therefore this is a Catalan linear matching satisfying the exact internal
depth-two residence condition.

#### Proof

Items 1--2 are direct enumeration of the displayed bijection.  Reconstructing
the lift gives maximum degree two; each connected component has one fewer
edge than vertices.  Since `252-210=42`, the result is a 42-path forest.
Finally, direct traversal of every component and all ten coordinate words
gives internal run histogram

\[
                  3^{42}4^7 5^3 6^4 7^8 9^1,
\]

with no run below three.  The independent audit reconstructs these facts
from the matching rather than trusting the displayed paths. \(\square\)

## 2. This is genuinely an interior rethread

Relative to the synchronized repaired source matching, 119 of the 210
diamond partners change.  The symmetric difference of the two perfect
matchings decomposes into alternating cycles whose half-length histogram is

\[
              2^9 3^7 4^5 5^2 6^2 7^3 8^1 9^1.     \tag{2.1}
\]

Thus the successful object is not an endpoint permutation of the old 42
paths.  It cuts and rethreads their interiors, exactly as the whole-path
obstruction required.  Conversely every move remains inside the exact
diamond perfect-matching space, so the immediate palettes never need to be
repaired afterwards.

## 3. Remaining flag debt

Internal windows of the new 42 paths cover both immediate palettes exactly.
The deeper internal misses are:

\[
\begin{array}{c|c|c}
q&\text{lower misses}&\text{upper misses}\\ \hline
2&6&10\\
3&2&2\\
4&0&1\\
5&0&0.
\end{array}
\]

There are 21 masks in total.  They are explicit in the audit JSON.  They may
be supplied by cross-fragment windows, just as four misses were supplied by
the prior colour-injective closure, but this has not yet been proved for the
new forest.

The endpoint runs likewise have histogram

\[
                1^{90}2^{80}3^{89}4^{43}5^{23}
                6^{19}7^6 8^4 10^1.
\]

They are not defects by themselves: after fragments are connected, common
coordinates merge across every Johnson seam.  The exact remaining finite
problem is to choose a component chronology and connector edges so that all
newly internal runs have length at least three and the 21 flag targets are
covered, followed by the erosion-envelope Hall audit.

## 4. Scope

The theorem proves existence of a residence-clean **central path forest** at
`m=5`.  It does not prove a fixed-decoration transparent history from the old
forest, recursively private sockets, primitive voltage, an all-depth final
chronology, or a lower compiler.  Equation (2.1) also does not imply a
bounded number of switches in general; the useful uniform target remains
bounded live boundary/debt, not bounded packet cardinality.

Reproduce with

```text
python3 scratch/audit_catalan_m5_residence_rethread_c4c6_20260731.py
```
