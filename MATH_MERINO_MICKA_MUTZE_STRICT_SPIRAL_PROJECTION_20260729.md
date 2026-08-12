# Rotational middle levels imply a strict-spiral Johnson cycle

Date: 2026-07-29

Status: theorem audit and independent live-source replay.  The existence
statement below is an unconditional consequence of Merino--Mička--Mütze.
The numerical defects are properties of the particular `combos.org`
shift-one cycle audited by `scratch/audit_knuth_symmetric_middle_k15.py`; they
are not impossibility results for every rotationally symmetric middle-levels
cycle.  The replay stdout is frozen, but the dynamically downloaded cycle is
not, so the numerical part is not yet a self-contained local certificate.

## 1. Projection theorem

Put

```text
k=2m+1,                 W=C(k,m+1)=k Cat_m,
N=W/k=Cat_m,
```

and let `rho` be cyclic coordinate rotation.  Theorem 1 of
[Merino--Mička--Mütze, *On a combinatorial generation problem of Knuth*](https://arxiv.org/abs/2007.07164)
gives, for every unit `s in Z_k`, a star-transposition ordering whose `k`
flip-position blocks are successive translates by `s`.  Deleting the
distinguished coordinate gives a middle-levels Hamilton cycle; with the
construction's compatible block origin and orientation, its state blocks are
carried to one another by `rho^s`.  Each block has length `2N`.  The sign of
`s` depends only on the left/right convention for `rho`.

### Theorem 1.1 (strict-spiral upper projection)

For every odd `k=2m+1` and every `s` coprime to `k`, there is a cyclic ordering

```text
B_0,B_1,...,B_(W-1)
```

of all rank-`m+1` subsets of `Z_k` such that

```text
|B_i triangle B_(i+1)|=2,
B_(i+N)=rho^s(B_i),
{B_i intersect B_(i+1): 0<=i<W}=C(Z_k,m)
```

with multiplicity one in the last display.  Thus `B` is a Johnson Hamilton
cycle, is a strict `k`-sheet spiral of voltage `s`, and is a perfect lower
depth-one rainbow.

#### Proof

Write the middle-levels Hamilton cycle in alternating form

```text
B_i, C_i, B_(i+1),
```

where `|B_i|=m+1` and `|C_i|=m`.  Both edges are inclusions, so

```text
C_i=B_i intersect B_(i+1)
```

and the two upper vertices differ by one deletion and one insertion.  The
middle-levels Hamilton cycle visits every lower vertex once, hence the `C_i`
are exactly all rank-`m` sets, once each.  This proves Johnson adjacency and
the lower rainbow.

The Merino--Mička--Mütze blocks have even length `2N`.  At the chosen block
boundary, the next block's starting state is the rotated starting state; the
translated flip-position recurrence then propagates that equality through
the entire block.  Taking the upper parity leaves `N` upper vertices per
block and gives `B_(i+N)=rho^s(B_i)`.  Translation is free on the two central
layers because

```text
gcd(k,m)=gcd(k,m+1)=1.
```

Since `s` is a unit, every displayed orbit has `k` elements.  Hamiltonicity
then forces the first `N` upper vertices to represent distinct orbits.  Their
quotient order is one cycle and its lift voltage is `s`.  This also proves
the assertion for odd composite `k`, in particular `k=15`.  □

## 2. What this closes in the Claude quotient model

The theorem makes the following constraints unconditional existence facts;
they no longer require SAT/CEGAR evidence.

| Quotient condition | Status from Theorem 1.1 |
|---|---|
| central rank-`m` and rank-`m+1` necklace freeness and layer size `Cat_m` | proved |
| exactly one selected Johnson-edge orbit over each lower central orbit | proved |
| weighted degree two at every upper-middle quotient vertex | proved |
| a coherent orientation and one connected quotient cycle | proved |
| a single physical Hamilton lift | proved |
| prescribed unit voltage `s` (hence the gcd lift condition) | proved |
| exact upper-middle owner deck | proved |
| perfect physical and quotient lower `q=1` rainbow | proved |

For `N>1`, connected two-regularity also excludes quotient self-loops: a
loop already contributes both incidences at its vertex and would isolate it.
This uses only central-layer freeness.  For composite `k`, deeper lower and
upper layers can have nontrivial stabilizers and still require the Burnside
orbit counts from the separate necklace audit.

None of the following is asserted by the paper or follows from the projection
argument:

1. coordinate residence for the erosion depth;
2. upper `q=1` coverage, or coverage of all larger interval unions;
3. cyclic lower `q=2,q=3,...` intersection coverage;
4. a cut simultaneously preserving residence and all shadow witnesses;
5. feasibility of the lower Hall compiler, a common erosion word, or its
   owner-compatible literalization.

In the terminology of `equi2.py`, the one-choice, degree, orientation,
component, physical-cycle, voltage, and lower-`q=1` clauses have an
unconditional solution.  The age/residence automaton, upper-shadow clauses,
deeper lazy support clauses, cut, and compiler remain genuine extra gates.

## 3. Exact shift-one audit at k=15

The checker has SHA-256

```text
8df79082426895cd3c7739971e9a09e5ad6137d3c3a46536fb10e331ab7c8880.
```

It downloads the published shift-one cycle, performs no optimization, and
checks the complete physical chronology.  It was replayed on the H100 CPU on
2026-07-29; exact stdout is frozen in
`scratch/audit_knuth_symmetric_middle_k15.out`.  The downloaded zip and
normalized cycle were not retained or hashed; the frozen stdout therefore
records an independently repeated observation, not a payload-complete
certificate.  Here

```text
k=15, m=7, r=8, W=C(15,8)=6435, N=Cat_7=429.
```

The strict-spiral conclusions pass exactly:

```text
middle-levels states                  12870 = 2W
upper-middle states                    6435 = W, all distinct
lower q1 intersections                 6435 / 6435
first quotient block distinct           429 / 429
strict orbit spacing                    true
spiral voltage                             1 mod 15
```

The extra gates fail for this chronology:

| Gate | Exact support | Missing |
|---|---:|---:|
| upper `q=1` unions, rank 9 | `4455/5005` | 550 |
| lower `q=2` intersections, rank 6 | `4455/5005` | 550 |
| lower `q=3` intersections, rank 5 | `2475/3003` | 528 |
| all strict upper ranks 9 through 15 | `8611/9949` | 1338 |

The minimum cyclic coordinate 1-run is two.  The short-run histogram begins

```text
length 2: 1500 runs
length 3:  480 runs
length 4:  630 runs
length 5:  120 runs
length 6:  300 runs
length 7:   15 runs
length 8:  360 runs,
```

with 6,435 runs in total.  At erosion depth `d=3`, residence requires every
internal one-run to have length at least four.  Hence there are 1,980 cyclic
short-run defects.  Cutting the cycle can make at most one cyclic one-run per
coordinate an endpoint run, so every cut leaves at least

```text
1980-15=1965
```

internal short runs.  Independently, a linear cut only removes cyclic
intervals and cannot fill any of the 1,338 cyclic upper holes.  Thus this
particular carrier has no residence-and-upper-safe cut.

The value two is the strongest automatic residence bound supplied by a
perfect lower first shadow.  Indeed, a one-run of length one for coordinate
`x` would make the two incident lower colours both equal to `B_i-{x}`,
contradicting the rainbow.  The audited cycle attains this forced minimum.

## 4. The known k=11 decorated repairs are quotient-global

The exact quotient comparison in
`scratch/compare_knuth_and_good_quotient.py` uses one edge choice over each of
the 42 lower-colour orbits.  Its two-coloured symmetric difference is
therefore balanced at every quotient vertex and decomposes into alternating
components.  The script SHA-256 is
`0c8aa84981483fcd70541b3402a92637638255d801c59defa8f278019838d461`.
The audited results are:

| Two quotient factors | Shared choices | Changed lower orbits | Symmetric difference | Alternating components |
|---|---:|---:|---:|---|
| published MMM shift-one cycle vs fresh `equi2_k11_rnd34` pass | `1/42` | `41/42` | 82 edges | one component on all 42 vertices |
| fresh `equi2_k11_rnd34` pass vs `D^3(sigma_sat_k11_465)` | `0/42` | `42/42` | 84 edges | one component on all 42 vertices |

The second row was independently recomputed directly from the frozen
465-letter word and selector.  The first row still inherits the dynamic
`combos.org` provenance caveat above.  In either row, switching from one
displayed factor to the other by components of their direct overlay requires
the unique spanning component.  Thus the known successful decoration is
global at quotient scale, not a local tweak of the canonical MMM factor.
This does not rule out a sequence of small switches through intermediate
factors; it rules out only a small-component decomposition of these two
direct differences.

## 5. Exact remaining conclusion

The literature theorem closes quotient topology, central ownership, unit
voltage, and the perfect lower first shadow for every odd `k`.  It does not
close the coefficient-one construction.  The audited canonical `k=15` cycle
shows sharply that strict spiral plus perfect lower `q=1` does not force
residence, upper `q=1`, or lower `q=2/q=3`.

The missing lower supports do not, by themselves, prove that every possible
sub-erosion compiler word is infeasible; that is a coupled Hall question.
What they do prove is that the canonical cycle does not carry the direct
all-depth cyclic flag tower used by the quotient sufficient condition.  The
remaining theorem must therefore select or modify a rotational Hamilton
cycle while controlling residence and both shadow towers, and then exhibit a
safe cut and one common lower compiler word.
