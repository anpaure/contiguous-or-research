# The SBE orientation gate is an exact Boolean endpoint-cut system

Date: 2026-07-31  
Status: exact all-parameter characterization and separation theorem; exact
one-component-flip criterion.  The finite `n=3,4` statements below concern
the authenticated chained structural forests only.  No all-parameter supply
of a feasible orientation, direct physical representatives, rooted support,
residence, deep shadows, or compiler is claimed.

## 0. Result and corrected quantifier order

Let `F` be an **undirected** Catalan linear forest at parameter `n`, and
write its path components as

\[
 P_j=u_j\cdots v_j\qquad(1\le j\le K).
\]

The endpoints may coincide when `P_j` is an isolated vertex.  Reversing a
path does not alter either direct occurrence graph.  It only chooses which
one of `u_j,v_j` is the omitted tail endpoint above and which is the omitted
head endpoint below.  Consequently simultaneous strict balanced expansion
(SBE) is exactly a system of cardinality inequalities in one Boolean
orientation bit per path component.

For each proposed orientation, two ordinary min-cuts either certify all the
inequalities or return a violated Boolean row.  The correct recursion order
for any argument that uses SBE is therefore

\[
 \boxed{
   \text{undirected structural forest }F
   \ \longrightarrow\ 
   \text{endpoint-orientation bits }x
   \ \longrightarrow\
   \text{common }Q
   \ \longrightarrow\
   \text{two direct SDRs and rooted physical support}.}
\]

In particular, SBE is not a condition to impose by first choosing `Q`.
The independently chosen guarded filler `G` on the isolated `c` rail is not
present in this system: SBE is structural-parent state belonging to `F`.

For the authenticated chained child at `n=4`, exactly `7600` of the
`2^14` bit orientations are SBE on both shores.  A single nontrivial path
flip repairs the stored orientation.  At `n=3`, none of the `2^5` bit
orientations is two-shore SBE, although direct common bases exist.  Thus the
Boolean system is exact for SBE and only sufficient for common-basis
existence.

## 1. Parameters and orientation-independent occurrence graphs

Put

\[
 M={2n\choose n},\qquad N={2n\choose n-1},\qquad
 P={2n\choose n-2},
\]

and

\[
 C=M-P,\qquad R=N-C,\qquad K=M-N=\operatorname{Cat}_n.
\tag{1.1}
\]

The vertex set of `F` is

\[
 X=\binom{[2n]}{n}.
\]

For an undirected child edge `q={t,h}`, put

\[
 L_q=t\cap h,\qquad U_q=t\cup h.
\]

The upper direct occurrence multigraph `G^-` contains the occurrence

\[
 L_q+x\longleftrightarrow U_q+x\qquad(x\notin U_q),
\tag{1.2}
\]

and the lower graph `G^+` contains

\[
 L_q-x\longleftrightarrow U_q-x\qquad(x\in L_q).
\tag{1.3}
\]

Their outer shores both have order `P`; their common middle shore is `X`.
Parallel occurrences retain their labels, although only their common
neighbourhood is relevant to the SBE inequalities.

### Proposition 1.1 (orientation independence)

Both labelled occurrence multigraphs, their two palette labels, and their
undirected physical edges depend only on the undirected forest `F`.  They
are unchanged by coherently reversing any component of `F`.

#### Proof

Exchanging `t` and `h` leaves `L_q`, `U_q`, the conditions
`x notin U_q` and `x in L_q`, and the unordered physical edge unchanged.
These data define (1.2)--(1.3).  Hence every labelled occurrence is
unchanged.  Only the auxiliary tail/head role changes.  \(\square\)

This proposition is about the direct **undirected-support** model.  It does
not assert preservation of a stronger ordered lift in which occurrences
must inherit child arrows.

## 2. Exact bit convention

Choose one bit `x_j` for each component and use the convention

\[
 x_j=0: u_j\longrightarrow v_j,
 \qquad
 x_j=1: v_j\longrightarrow u_j.
\tag{2.1}
\]

Along a coherently oriented path, every vertex except the terminal head is
a tail, and every vertex except the initial tail is a head.  Therefore the
terminal banks omitted from the upper tail image and lower head image are

\[
\begin{aligned}
 Z_x^-&=\{v_j:x_j=0\}\cup\{u_j:x_j=1\},\\
 Z_x^+&=\{u_j:x_j=0\}\cup\{v_j:x_j=1\}.
\end{aligned}
\tag{2.2}
\]

The endpoint images used by the two pulled-back direct matroids are

\[
 T_x^-=X\setminus Z_x^-,\qquad T_x^+=X\setminus Z_x^+.
\tag{2.3}
\]

For an isolated component `u_j=v_j`, the bit is a dummy: both choices give
the same two terminal banks.

## 3. The simultaneous Boolean cut theorem

For one shore `sigma in {-,+}` and an outer family `A`, let

\[
 \Gamma^\sigma(A)=N_{G^\sigma}(A)\subseteq X.
\tag{3.1}
\]

SBE gives weight `R/N` to a vertex in the endpoint image and weight `1` to
a terminal.  After scaling by `N`, the weight is `R` on `T_x^sigma` and
`N=R+C` on `Z_x^sigma`.  Thus

\[
 w_x^\sigma(S)=R|S|+C|S\cap Z_x^\sigma|
 \qquad(S\subseteq X).
\tag{3.2}
\]

### Theorem 3.1 (exact endpoint-orientation cut system)

The orientation `x` is SBE on both shores if and only if the following two
families of inequalities hold for every outer family `A`:

\[
\boxed{
 R|\Gamma^-(A)|+
 C\sum_{j=1}^K\left(
   (1-x_j){\bf1}_{v_j\in\Gamma^-(A)}+
       x_j {\bf1}_{u_j\in\Gamma^-(A)}
 \right)
 \ge N|A|,}
\tag{3.3}
\]

and

\[
\boxed{
 R|\Gamma^+(A)|+
 C\sum_{j=1}^K\left(
   (1-x_j){\bf1}_{u_j\in\Gamma^+(A)}+
       x_j {\bf1}_{v_j\in\Gamma^+(A)}
 \right)
 \ge N|A|.}
\tag{3.4}
\]

#### Proof

For the upper shore, (2.2) says that the selected terminal in component
`j` is `v_j` when `x_j=0` and `u_j` when `x_j=1`.  Therefore the sum in
(3.3) is exactly

\[
 |\Gamma^-(A)\cap Z_x^-|.
\]

By (3.2), (3.3) is precisely the scaled weighted Hall inequality

\[
 |A|\le {1\over N}w_x^-(\Gamma^-(A)).
\]

These inequalities for all `A` are the definition of upper SBE.  The lower
terminal choice is complementary on each nontrivial component, giving
(3.4).  Applying the same argument below proves the equivalence on both
shores.  \(\square\)

### Corollary 3.2 (compressed literal row)

Every row in (3.3) or (3.4) is one signed cardinality row.  To see this,
for the chosen shore write `e_{j,0}^sigma,e_{j,1}^sigma` for the terminal
selected by bit `0,1`.  Thus

\[
 (e_{j,0}^-,e_{j,1}^-)=(v_j,u_j),\qquad
 (e_{j,0}^+,e_{j,1}^+)=(u_j,v_j).
\tag{3.5}
\]

Let `B^sigma(A)` be the number of components for which both endpoint
indicators in `Gamma^sigma(A)` equal one, and let `J^sigma(A)` be the set
for which exactly one equals one.  For `j in J^sigma(A)`, define the
literal

\[
 \ell_j^\sigma(A)=
 \begin{cases}
 x_j,&e_{j,0}^\sigma\notin\Gamma^\sigma(A),\quad
      e_{j,1}^\sigma\in\Gamma^\sigma(A),\\
 1-x_j,&e_{j,0}^\sigma\in\Gamma^\sigma(A),\quad
      e_{j,1}^\sigma\notin\Gamma^\sigma(A).
 \end{cases}
\tag{3.6}
\]

Then the row is exactly

\[
 \boxed{
 \sum_{j\in J^\sigma(A)}\ell_j^\sigma(A)
 \ge
 \left\lceil{N|A|-R|\Gamma^\sigma(A)|\over C}\right\rceil
 -B^\sigma(A).}
\tag{3.7}
\]

A nonpositive right side is tautological; a right side larger than
`|J^sigma(A)|` is an orientation-independent failure.  Singleton
components contribute a constant, never a literal.

#### Proof

Each component contributes one to
`|Gamma^sigma(A) cap Z_x^sigma|` when both endpoints lie in the
neighbourhood, zero when neither does, and the literal (3.6) when exactly
one does.  Substitute this decomposition into (3.3) or (3.4) and use
integrality of the left side.  \(\square\)

### Corollary 3.3 (closed-middle-set form)

For `S subseteq X`, put

\[
 A^\sigma(S)=\{o\in O^\sigma:N_{G^\sigma}(o)\subseteq S\}.
\tag{3.8}
\]

It is equivalent to impose

\[
 R|S|+C|S\cap Z_x^\sigma|\ge N|A^\sigma(S)|
 \qquad(S\subseteq X)
\tag{3.9}
\]

on both shores.

#### Proof

If (3.9) holds and `S=Gamma^sigma(A)`, then
`A subseteq A^sigma(S)`, so (3.3) or (3.4) follows.  Conversely, apply
weighted Hall to `A^sigma(S)` and use
`Gamma^sigma(A^sigma(S)) subseteq S`.  \(\square\)

## 4. Exact min-cut separation and Boolean master

For a fixed orientation `x`, each shore has the following closure network:

* source to every outer vertex, capacity `N`;
* outer vertex to each middle neighbour, infinite capacity;
* middle vertex `D` to the sink, capacity
  `R+C*1[D in Z_x^sigma]`.

If `cut_x^sigma` is its minimum cut, then

\[
 \Delta_x^\sigma
 =NP-\operatorname{cut}_x^\sigma
 =\max_A\bigl(N|A|-w_x^\sigma(\Gamma^\sigma(A))\bigr).
\tag{4.1}
\]

Hence `x` passes a shore exactly when `Delta_x^sigma=0`.  When the value is
positive, the source-side outer family yields a violated row (3.7).

This gives a proof-exact branch-and-cut formulation:

1. the master has only the `K` path-orientation bits, plus any genuine
   endpoint pins;
2. two min-cuts separate a proposed integral orientation;
3. each failed shore returns one valid signed cardinality row (3.7).

The separation oracle is polynomial.  No claim is made that the resulting
integer feasibility problem, with cuts from both shores, is itself a
network matrix, 2-SAT instance, or polynomial-time solvable.

## 5. Exact one-flip preservation and repair

Define the scaled slack of a cut by

\[
 s_x^\sigma(A)=
 R|\Gamma^\sigma(A)|+C|\Gamma^\sigma(A)\cap Z_x^\sigma|-N|A|.
\tag{5.1}
\]

Fix a component `j`, let `z_j^sigma` be its currently selected terminal on
shore `sigma`, and let `bar z_j^sigma` be the endpoint selected after
flipping `x_j`.  Put

\[
 \delta_j^\sigma(A)=
 {\bf1}_{\bar z_j^\sigma\in\Gamma^\sigma(A)}-
 {\bf1}_{z_j^\sigma\in\Gamma^\sigma(A)}
 \in\{-1,0,1\}.
\tag{5.2}
\]

### Theorem 5.1 (one-flip margin criterion)

The exact slack identity is

\[
 s_{x\oplus e_j}^\sigma(A)
 =s_x^\sigma(A)+C\delta_j^\sigma(A).
\tag{5.3}
\]

Consequently:

1. if `x` is SBE, the flip preserves shore `sigma` if and only if every
   cut that loses its selected terminal has old slack at least `C`;
2. for an arbitrary old orientation, the flip repairs shore `sigma` if
   and only if
   \[
   \begin{array}{c|c}
   \delta_j^\sigma(A)&\text{required old slack}\\ \hline
   +1&s_x^\sigma(A)\ge -C,\\
    0&s_x^\sigma(A)\ge 0,\\
   -1&s_x^\sigma(A)\ge C;
   \end{array}
   \tag{5.4}
   \]
3. simultaneous preservation or repair holds exactly when the corresponding
   condition holds on both shores.

#### Proof

Only the chosen terminal of component `j` changes.  Its contribution to
(5.1) changes by `C` times (5.2), proving (5.3).  The three cases in (5.4)
are exactly the condition that the new slack be nonnegative.  When every
old slack is nonnegative, only the `delta=-1` case can fail, giving the
first assertion.  \(\square\)

For a feasible old orientation, the worst losing cut can also be found by
pinned min-cuts: forbid every outer neighbour of `bar z_j^sigma`, and in
turn force one outer neighbour of `z_j^sigma`.  Taking the worst result
over those choices enforces

\[
 z_j^\sigma\in\Gamma^\sigma(A),\qquad
 \bar z_j^\sigma\notin\Gamma^\sigma(A).
\]

If no neighbour of the old terminal remains eligible after those
exclusions, the losing-cut family is empty and safety is vacuous.

Thus safe single flips have a polynomial exact audit.  More generally, a
set of flips changes every cut slack by the sum of its endpoint-membership
changes; there is no hidden `Q` term.

## 6. Postorientation lemma for a recursive forest proof

### Lemma 6.1 (postorientation before the next common basis)

Suppose a direct undirected-support construction has produced a Catalan
linear forest `F'`.  If the simultaneous endpoint-cut system (3.3)--(3.4)
for `F'` has a solution `x'`, then the components of `F'` may be coherently
oriented according to `x'` without changing:

* either direct occurrence multigraph;
* either occurrence palette;
* the undirected physical degrees; or
* acyclicity and component count of `F'`.

For that orientation, SBE puts the constant vector `C/N` in both strict
pulled-back direct base polytopes.  Matroid-intersection integrality then
supplies a strict common basis `Q` for the **next** lift.

#### Proof

The first four assertions are Proposition 1.1 and the fact that reversing
a component preserves an undirected forest.  The endpoint-cut theorem
gives SBE on both shores.  The strict balanced-expansion common-basis
theorem then gives the common basis.  \(\square\)

This lemma does not preserve a previously fixed `Q` or previously fixed
direct SDRs.  Reorientation changes the tail/head injections, so those
objects must be selected after the orientation.  Likewise, SBE alone does
not supply representative capacity, rooted graphic support, or residence.

In particular, a synchronized `Q`/SDR packet with the structural forest
`F` and its orientation fixed stays inside one endpoint-orientation fibre:
it changes none of the rows (3.3)--(3.4), so it cannot repair a failed SBE
orientation.  If such a packet changes the **output** undirected forest,
then it can affect the next-stage Boolean system only through that new
forest.  Conversely, reversing an entire path is not a bounded `Q` packet;
although it preserves the occurrence catalogue, it changes the endpoint
injections and therefore requires the common basis and representatives to
be certified again.

If a stronger construction genuinely pins the direction of a component,
the corresponding equation `x_j=0` or `x_j=1` must be added to the Boolean
master.  Such ordered constraints can make an otherwise feasible SBE
system infeasible.

## 7. Exact finite calibration

The authoritative orientation result is Proposition 1.3 of

```text
MATH_THEOREM_R_CATALAN_EDGEWISE_ROOTED_DOUBLE_RAINBOW_EAR_AND_TWO_PARENT_GATE_20260731.md
```

on the chained witness

```text
scratch/catalan_direct_edgewise_side_lift_recursive_n3_n6_20260731.witness.json
```

with the SBE min-cut implementation in

```text
scratch/audit_catalan_strict_balanced_expansion_n3_n7_20260731.py
```

The exact finite facts are:

* `n=3`: the component orders are `2,2,14,1,1`; none of the `2^5` bit
  strings is SBE on both shores.  The two singleton bits are dummy, so
  there are only eight effective endpoint choices.  Direct common bases
  nevertheless exist, proving that SBE is not necessary.
* `n=4`: the component orders are
  `6,9,9,8,2,2,1,14,1,6,8,1,1,2`.  Exactly `7600/2^14` bit strings are SBE
  on both shores.  Four bits are dummy singleton reversals, so this is
  `475/2^10` effective endpoint choices.
* The stored `n=4` orientation has scaled violations `(upper,lower)=(14,0)`.
  Its upper minimum cut has 18 outer vertices and 53 middle neighbours,
  six of them terminals, so with `(N,R,C)=(56,14,42)` it reads
  
  \[
        56\cdot18=1008>14\cdot53+42\cdot6=994.
  \]
  
  Reversing component `4`, whose endpoints are `0x4d,0x5c`, gives `(0,0)`.
  Reversing component `13`, whose endpoints are `0xa9,0xe8`, also gives
  `(0,0)`.  Thus the statement that one path flip repairs the stored
  orientation has two literal witnesses in the stored component order.

The last flip check is only a reorientation audit.  It does not assert that
either repaired orientation automatically retains a previously frozen
`Q`, SDR pair, or rooted physical extension.

An independent solver-free replay is frozen as

```text
scratch/audit_threadD_catalan_sbe_endpoint_orientations_n3_n4_20260731.py
scratch/threadD_catalan_sbe_endpoint_orientations_n3_n4_20260731.audit.json
```

It reconstructs both occurrence graphs after every single path reversal,
enumerates all effective endpoint choices at `n=3,4`, and runs the exact
integer min-cut oracle.  The script SHA-256 is
`c57f71821efef29e60b012ddfa9986c2735f5f8e447b938c6ee672cbb3ddac84`;
the JSON SHA-256 is
`8dac95c2369dd944d82a1c55027509884421fedcae6eb883d4f7e7a10c92b707`,
with canonical payload
`d341b398634c257856e33d0fb9c540d050ca608a7080643f0b04c1e02abb6bbc`.

## 8. Exact scope

The following statements are proved here:

1. direct occurrence graphs are orientation-independent;
2. simultaneous two-shore SBE is exactly (3.3)--(3.4), equivalently the
   compressed literal system (3.7);
3. fixed-orientation separation needs two ordinary min-cuts;
4. one-flip preservation and repair are exactly the margin conditions
   (5.3)--(5.4); and
5. after an undirected output forest is built, an SBE orientation may be
   chosen before the next common basis without changing that forest.

The following are not consequences:

* every Catalan forest has an SBE orientation;
* SBE is necessary for a direct common basis;
* an SBE orientation has rooted physical representatives;
* a fixed `Q` survives a component flip;
* the guard filler `G` is forced to equal the structural parent `F`; or
* the resulting recursion is residence-safe or proves the full
  contiguous-OR equality.

The reusable preservation target is therefore the feasibility of the
endpoint Boolean cuts for the newly produced **structural** forest, followed
by integral selection of `Q`, the two SDRs, and rooted support.  Guarded
`c`-rail filling remains an independent two-parent quantifier.
