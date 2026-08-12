# Exact both-`q1` rows on the canonical even factor catalogue

Date: 2026-07-29  
Status: proved theorem and source audit; no solver run.  This note treats
only the factor and both-`q1` layers.  Residence, connectivity, opening, and
the literal compiler are not claimed here.

## 0. Result

Let

\[
 K=2r,\qquad n=K-1=2r-1,
\]

let `rho` rotate the `n` old coordinates and fix `z`, and use the canonical
undirected edge-orbit catalogue `E_K` of
`MATH_THEOREM_AD_CANONICAL_SECTION_COMPONENT_CATALOGUE_20260729.md`.
For an edge orbit `e`, write

\[
 L(e)=[X\cap Y]_\rho,\qquad U(e)=[X\cup Y]_\rho,       \tag{0.1}
\]

where `XY` is any physical edge in `e`.  These target orbits do not depend
on the representative edge.

If `O` is a lower or upper `q1` target orbit, put

\[
 h_O=|\operatorname {Stab}_{C_n}(T)|=\frac n{|O|}
 \quad(T\in O),                                         \tag{0.2}
\]

and define `P_L(O)={e:L(e)=O}` and `P_U(O)={e:U(e)=O}`.

### Theorem 0.1 (literal coverage and exact stabilizer coefficient)

For every invariant factor incidence vector `y in {0,1}^{E_K}` and every
literal target `T in O`, its physical lower and upper edge loads are

\[
 \lambda_L(T)=h_O\sum_{e\in P_L(O)}y_e,\qquad
 \lambda_U(T)=h_O\sum_{e\in P_U(O)}y_e.                \tag{0.3}
\]

Consequently the complete literal lower- and upper-`q1` conditions are
exactly

\[
 \sum_{e\in P_L(O)}y_e\geq1\quad(O\text{ lower}),
 \qquad
 \sum_{e\in P_U(O)}y_e\geq1\quad(O\text{ upper}).     \tag{0.4}
\]

They use no auxiliary variables and no window, width, component, or voltage
selectors.  Formula (0.3), rather than a unit-coefficient occurrence ledger,
must be used whenever loads or excess occurrences matter.

For `K=16`, (0.4) consists of exactly `764+764=1,528` cover
rows on the existing `27,456` edge variables.  The two palettes together
contain exactly `54,912` positive literal incidences.  Together with the
factor equations, the complete undirected factor-plus-both-`q1` PB core is
therefore

```text
binary variables                    27,456
weighted degree-two equations          858
lower-q1 cover inequalities             764
upper-q1 cover inequalities             764
q1 positive literal incidences        54,912
q1 auxiliary variables                     0
```

This is complete for arbitrary successor permutations and arbitrary zero,
nonunit, or unit component voltages.  It does not require that the quotient
or physical factor be connected.

## 1. General proof of the load formula

The action of `C_n` on physical middle vertices and on physical Johnson
edges is free.  Thus every `e in E_K` contains exactly `n` physical edges.
Intersection and union commute with rotation, so all lower targets of the
edges in `e` form `L(e)`, and all upper targets form `U(e)`.

Fix `e in P_L(O)` and one target `T in O`.  The equivariant map from the
`n` edges in `e` to their intersections is the orbit map `C_n -> O`.
Every fibre has cardinality

\[
                         |C_n|/|O|=h_O.                 \tag{1.1}
\]

The edges in that fibre are distinct because the edge action is free.
Therefore selecting `e` contributes exactly `h_O` physical occurrences to
every literal target in `O`.  Summing selected edge orbits proves the first
identity in (0.3).  The union proof is identical.

Every literal target in `O` is covered if and only if the common load in
(0.3) is positive.  Since `h_O>=1` and the variables are Boolean, this is
equivalent to the support row (0.4).  This proves Theorem 0.1.  Notice that
the proof never traverses a component.  Every selected factor edge is
already a literal interval of length two on its physical cycle.

More generally, a fixed rank-`r-1` target is the intersection of

\[
                         \binom{r+1}{2}                 \tag{1.2}
\]

physical middle edges, and a fixed rank-`r+1` target is the union of the
same number.  Hence a target orbit with stabilizer order `h_O` has exactly

\[
             |P_L(O)|=|P_U(O)|
               =\frac1{h_O}\binom{r+1}{2}              \tag{1.3}
\]

provider edge orbits, with the equality interpreted in the appropriate
lower or upper palette.  Equation (1.3) also follows by dividing the
`|O| binom(r+1,2)` physical providers by the free edge-orbit size `n`.

## 2. Exact `K=16` necklace census

Now set `r=8` and `n=15`.  A middle mask is either

* an `A` owner: eight old coordinates and no `z`; or
* a `B` owner: seven old coordinates and `z`.

Both old ranks have free rotation action because
`gcd(15,8)=gcd(15,7)=1`.  There are

\[
                  \binom{15}{7}/15
                = \binom{15}{8}/15=429                \tag{2.1}
\]

owner orbits on each shore.

The four `q1` palettes and their edge types are:

| physical target | old rank | provider edge types |
|:--|--:|:--|
| lower, no `z` | 7 | `AA` intersection and `AB` lower endpoint |
| lower, with `z` | 6 | `BB` intersection |
| upper, no `z` | 9 | `AA` union |
| upper, with `z` | 8 | `BB` union and `AB` upper endpoint |

Old ranks seven and eight are free and give `429` target orbits each.
For old rank six, Burnside gives

\[
 \frac1{15}\left(\binom{15}{6}+2\binom52\right)
   =\frac{5005+20}{15}=335.                             \tag{2.2}
\]

Indeed, the only possible nontrivial stabilizer has order three: weight six
is divisible by three but not by five or fifteen.  The two rotations of
order three each fix the same ten unions of two of the five length-three
coordinate cycles.  These ten masks form exactly two target orbits of size
five.  Thus rank six has

\[
                    333\text{ orbits of size }15,
                    \quad2\text{ orbits of size }5.     \tag{2.3}
\]

Complementation gives the identical statement at old rank nine.  In the
canonical integer convention of
`scratch/k16_even_necklace_q1_factor_20260729.py`, the two old rank-six
representatives are `3171` and `5285`; their rank-nine complement orbits are
represented canonically by `7399` and `11627`.

It follows that each lower and upper palette has

\[
                         429+335=764                    \tag{2.4}
\]

rows.  The exact provider census is

| palette | rows | provider variables per row |
|:--|--:|:--|
| lower, no `z` | 429 | `28 AA + 8 AB = 36` |
| lower, with `z`, generic | 333 | `36 BB` |
| lower, with `z`, exceptional | 2 | `12 BB` |
| upper, no `z`, generic | 333 | `36 AA` |
| upper, no `z`, exceptional | 2 | `12 AA` |
| upper, with `z` | 429 | `28 BB + 8 AB = 36` |

For example, a lower no-`z` target has seven old coordinates.  Its two
added labels can either both be among the eight remaining old coordinates,
giving `binom(8,2)=28` `AA` edges, or be `z` and one remaining old label,
giving eight `AB` edges.  The other free mixed palette is complementary.
The two exceptional lower-with-`z` orbits have `h_O=3`, so (1.3) gives
`36/3=12` provider variables per row.  The exceptional upper rows are their
complements.

The exact physical load equations on those four short orbits are therefore

\[
                  \lambda(T)=3\sum_{e\in P(O)}y_e.      \tag{2.5}
\]

One selected provider orbit covers all five literal targets, three times
each.  Thus the Boolean cover clause still has coefficient one, but its
first witness consists of fifteen occurrences and forces ten occurrences
beyond one-per-literal coverage.  Treating a selected provider as one
physical occurrence per exceptional target is unsound.

Finally, the provider-literal total in one complete lower palette is

\[
 429\cdot36+333\cdot36+2\cdot12=27,456,               \tag{2.6}
\]

and the upper total is the same.  This is also forced structurally: every
edge-orbit variable has exactly one lower and exactly one upper target-orbit
label.  Hence the two palette families contain exactly `54,912` positive
literal incidences.

## 3. Oriented successor form and voltage independence

Let `A_K` be the `54,912`-dart oriented catalogue, with reverse dart
`a -> bar(a)`.  An oriented factor is encoded by one-out, one-in, and
`x_a+x_bar(a)<=1`.  Give a dart `a=(i,j,p)` the labels

\[
 L(a)=[U_i\cap\rho^pU_j]_\rho,\qquad
 U(a)=[U_i\cup\rho^pU_j]_\rho.                         \tag{3.1}
\]

For the underlying undirected orbit `e={a,bar(a)}`, the exact linkage is

\[
                         y_e=x_a+x_{\bar a}.             \tag{3.1a}
\]

The reverse mutex makes the right-hand side Boolean.  Conversely, an
equivariant orientation of every decoded physical cycle chooses exactly one
of the two summands for every selected `e`.

The exact oriented cover rows are

\[
 \sum_{a:L(a)=O}x_a\ge1,
 \qquad
 \sum_{a:U(a)=O}x_a\ge1.                               \tag{3.2}
\]

No undirected linking variables are needed.  Every undirected provider has
two reverse darts, so the row widths are `72` generically and `24` on the
four exceptional rows.  The two oriented palette families contain
`109,824` positive literal incidences.

The selected outgoing dart at owner `i` supplies an arbitrary successor
`sigma(i)` and phase `p_i`.  On a quotient component `C`, the voltage is
`sum_{i in C}p_i mod 15`.  Neither that sum nor `gcd(15,v_C)` occurs in
(3.1)--(3.2): selecting a dart always selects all fifteen rotations of its
physical edge.  Therefore (3.2) is exact for every component decomposition
and every voltage, including voltage zero and nonunit voltage.

Changing the canonical section by `U_i -> rho^{q_i}U_i` changes the stored
phase to `p_i+q_i-q_j` but leaves the underlying physical edge orbit and
both labels in (3.1) unchanged.  Thus these rows are section-gauge invariant.
A global coordinate multiplier merely permutes target rows.

## 4. Source audit

The existing source

```text
scratch/k16_even_necklace_q1_factor_20260729.py
```

implements exactly the support version of the theorem:

1. `canonical_edge` constructs the `27,456` free physical edge orbits;
2. `color(u & v)` and `color(u | v)` construct `L(e)` and `U(e)`;
3. `lower_providers` and `upper_providers` partition the edge variables by
   those labels;
4. the two loops over provider maps add precisely (0.4);
5. `lift_and_audit` rebuilds all fifteen physical rotations before checking
   degree and records the support sets of the canonical colours.

The hard assertions in that source agree with the theorem: `858` owner
orbits, `27,456` edge orbits, `764` rows per palette, the splits
`429+335`, quotient incidence degree `64`, and `28` quotient loops.

The code intentionally stores only support rows.  It is sound for literal
coverage by Theorem 0.1, but its provider maps alone are not an exact
physical load ledger on the four short target orbits.  Any future exact-load,
rainbow, or excess objective must attach coefficient `h_O`, equal to three
on those rows, as in (0.3) and (2.5).

## 5. Exact boundary of the result

Proved here:

* exact literal both-`q1` equivalence on the complete canonical factor
  catalogue;
* all target-orbit stabilizer coefficients;
* the full `K=16` row widths and incidence counts;
* independence from successor topology and component voltages;
* zero auxiliary variables and zero width selectors for this layer.

Not proved here:

* residence at least four;
* connectivity or a prescribed voltage condition;
* preservation after physically opening components;
* any deeper shadow width;
* literal compiler feasibility.

In particular, cyclic both-`q1` coverage of a factor is not automatically
both-`q1` coverage of an opened word: deleting cut edges removes their
lower and upper witnesses, and new seams must be entered in the separate
opening ledger.
