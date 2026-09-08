# The standard-GK short boundary has two distinct capacity-two theorems

Date: 2026-08-01  
Lane: Thread D / SCD short-triangle tight augmenters  
Status: all-dimensional forward capacity-two theorem; exact reverse
two-orientation reduction and finite verification through `m=12`; paired-ear
and graphic completion remain separate.

## 0. Scope and verdict

Let `G` have order `2m-3`, let `L_sh` be the standard Greene--Kleitman
short-top family in rank `m-1`, and put

\[
             U_sh=\partial^+L_sh\subseteq {G\choose m}.
\]

There are two different statements that can be called a capacity-two
matching on this boundary.

1. **Forward:** every short top is a demand and every `U in U_sh` has
   capacity two.  This holds for every `m>=3`, by an all-cut proof.
2. **Reverse:** every `U in U_sh` is a demand and every short top has
   capacity two.  This is equivalent to an exact two-orientation cut.  A
   deterministic O3 audit verifies it through `m=12`, even after every `U`
   is restricted to two canonical providers.  An all-dimensional proof is
   not supplied here.

Neither statement is the fixed-`M_0` paired-ear theorem.  In the general
paired ear, the first and second rotations independently choose
`U_0=L+b_0` and `U_1=L+b_1`; they require injectivity of `U_0`, of `U_1`,
and of `V_1=S+b_1=U_1-x`.  The common-label restriction `b_0=b_1` uses one
`U` simultaneously for the colours `zU,aU` and the rooted head `P(U)`,
and also uses `V=U-x` for `Q(V)`.  Capacity two in either anonymous
projection does not imply these typed SDR, endpoint, or graphic rows.

## 1. Exact sizes and degrees

Write

\[
 c=|L_sh|=\operatorname {Cat}_{m-1}.
\]

The short-boundary identity proved in
`MATH_THEOREM_SCD_SHORT_TRIANGLE_AUGMENTER_EAR_GRAMMAR_20260801.md` is

\[
 \begin{aligned}
 I_m=|U_sh|
   &=\operatorname {Cat}_m-2\operatorname {Cat}_{m-1}\\
   &={2(m-2)\over m+1}\,c.                         \tag{1.1}
 \end{aligned}
\]

In the incidence graph `L subset U`, every short top has degree exactly
`m-2`.  If `tau(U)` is the first time the walk of `U` reaches level `-2`,
then

\[
 d(U)=\#\{L\in L_sh:L\subset U\}={\tau(U)\over2}+1,
 \qquad 2\le d(U)\le m-1.                           \tag{1.2}
\]

The two total-capacity ledgers are consequently

\[
 2I_m-c={3(m-3)\over m+1}c                         \tag{1.3}
\]

in the forward direction and

\[
 2c-I_m={6\over m+1}c                              \tag{1.4}
\]

in the reverse direction.  The forward total cut is tight at `m=3`;
the reverse total cut always has positive slack.

## 2. All-dimensional forward theorem

### Theorem 2.1 (short demands, boundary capacity two)

For every `m>=3`, all members of `L_sh` can be assigned to containing
members of `U_sh` so that no member of `U_sh` is used more than twice.

#### Proof

Let `X subseteq L_sh` and let `N(X)` be its upper-boundary neighbourhood.
Counting incidences between `X` and `N(X)` and using (1.2) gives

\[
              (m-2)|X|\le (m-1)|N(X)|.              \tag{2.1}
\]

Because `(m-2)/(m-1)>=1/2`, this implies

\[
                         |X|\le2|N(X)|              \tag{2.2}
\]

for every `X`.  Clone every boundary vertex twice and apply Hall.  \(\square\)

At `m=3`, the two short tops have the same unique boundary neighbour, so
the total cut is the unique dimension-minimal tight example.  For `m>3`,
(2.1) gives strict multiplicative slack for every nonempty cut.

## 3. Reverse matching and its exact cut

The reverse statement has a useful two-provider compression.  Encode a
rank-`m` target `U` as a walk with absent step `+1` and present step `-1`.
Its minimum is `-3`.  Let `t_1,t_2` be the first down-steps which reach
levels `-1,-2`, respectively, and let

\[
                 L_j(U)=U-\{t_j\},\qquad j=1,2.     \tag{3.1}
\]

Flipping either step raises the subsequent suffix by two.  Before `t_j`
the walk is no lower than `-(j-1)`, and after it the minimum is `-1`.
Thus both `L_1(U),L_2(U)` are short tops.  They are distinct.

Define a graph `H_m` on vertex set `L_sh` with one edge

\[
                       e_U=L_1(U)L_2(U)              \tag{3.2}
\]

for each `U in U_sh`.  Choosing one of the two canonical providers for
every target, with short-top capacity two, is exactly an orientation of
`H_m` with indegree at most two.

### Theorem 3.1 (exact reverse min--max)

The canonical reverse capacity-two matching exists if and only if

\[
                    |F|\le2|V(F)|                  \tag{3.3}
\]

for every edge set `F subseteq E(H_m)`.  If it fails, a set maximizing

\[
                    |F|-2|V(F)|                    \tag{3.4}
\]

is an exact Hall certificate and is obtainable by one bipartite min-cut.

#### Proof

Make every target edge a left vertex adjacent to its two endpoints and
give every endpoint capacity two.  Capacitated Hall says precisely
`|F|<=2|V(F)|` for all target sets `F`.  Equivalently, orient each edge
toward its selected endpoint.  \(\square\)

The graph is bipartite: the two short tops attached to `U` exchange the
present coordinates `t_1,t_2`, and `t_2-t_1` is odd because the intervening
walk is a balanced excursion followed by one down-step.  Hence the parity
of the sum of present coordinate indices changes across every edge.  This
parity fact alone does not prove (3.3).

## 4. Exact finite audit

`scratch/audit_threadD_scd_short_phase0_capacity2_20260801.cpp` independently
enumerates `L_sh,U_sh`, solves both the unrestricted reverse b-matching and
the canonical two-provider matching, and checks the counts.  The H100 CPU
run used one O3 process, 3.39 seconds and 32,212 KiB maximum RSS.

\[
\begin{array}{c|rrrrrrrrrr}
m&3&4&5&6&7&8&9&10&11&12\\ \hline
c&2&5&14&42&132&429&1430&4862&16796&58786\\
I_m&1&4&14&48&165&572&2002&7072&25194&90440\\
\nu_2&1&4&14&48&165&572&2002&7072&25194&90440.
\end{array}                                         \tag{4.1}
\]

Here `nu_2` is already the matching number after restriction to the two
canonical providers (3.1), so the unrestricted matching has the same full
rank.  The canonical graph is connected and bipartite in every audited
dimension.

One tempting fractional proof does not extend: assigning each target
uniformly over all of its `d(U)` providers gives maximum provider loads

\[
 1/2,5/6,13/12,77/60,29/20,223/140,481/280,
 4609/2520,4861/2520,\ldots
\]

for `m=3,...,11`, namely `H_(m-1)-1` in the extremal row, and it first
exceeds two at `m=12`.  Nevertheless the integral two-provider matching
still exists at `m=12`.  Therefore the finite result is not evidence for
that symmetric fractional shortcut; the remaining all-dimensional gate is
the sparse cut (3.3).

## 5. Relation to the paired-ear problem

For one short chain `S<L=S+x`, the two rotations may choose independent
`b_0,b_1 notin L` and expose

\[
 U_0=L+b_0,\qquad U_1=L+b_1,\qquad
 V_1=S+b_1=U_1-x.                                  \tag{5.1}
\]

Across a serviced source family, resource disjointness requires

\[
 U_{0,S}\text{ all distinct},\quad
 U_{1,S}\text{ all distinct},\quad
 V_{1,S}\text{ all distinct}.                     \tag{5.2}
\]

The first row is ordinary Hall, while the last two form a coloured
three-partite SDR.  The restriction `b_0=b_1` is the stricter square-SDR.
Neither is either anonymous capacity-two problem above.  After (5.2), the
rooted endpoint tickets transform as

\[
 C\to A
 \longmapsto
 B\to C\to P(U_0),\quad A\to Q(V_1),               \tag{5.3}
\]

and the induced short-to-short arcs must be acyclic, or independent in the
contracted background graphic matroid.  Thus Theorem 2.1 is a genuine
boundary-capacity lemma and Theorem 3.1 is a useful reverse compression,
but neither closes the fixed-`M_0` coloured three-partite SDR/forest gate
(whose same-label restriction is the square-SDR).

## 6. Frozen artifacts

* `scratch/audit_threadD_scd_short_phase0_capacity2_20260801.cpp`;
* `scratch/threadD_scd_short_phase0_capacity2_20260801.audit.json`.
