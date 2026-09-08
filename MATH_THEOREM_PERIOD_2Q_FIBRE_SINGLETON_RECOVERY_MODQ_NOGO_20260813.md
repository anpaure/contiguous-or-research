# Period-`2q` fibre inflation cannot recover the singleton conformal residue

Date: 2026-08-13  
Status: exact modular no-go and proof-safe structured-leave boundary  
Companion positive theorem:
`MATH_THEOREM_GRAPH_OWNER_COMPLEMENTARY_FIBRE_WHOLE_RAIL_LIFT_20260813.md`  
Companion theorem SHA-256:
`cb0921bf5b674f2019ddcb37070226c3a4ccdcf541060f4b4e2a9b679b425f09`

## 1. The auxiliary-current invariant

Let `q >= 2`.  Let `O` be a rank-`R` owner and let `F_O` be any closed
pure rail of period `2q`, core size `R-q`, and `q`-window owners, with
`O` occurring as one distinguished owner of the rail.  Write

\[
 f_O=\mathbf 1_{\operatorname{supp}F_O},\qquad
 a_O=f_O-e_O.                                      \tag{1.1}
\]

Thus `a_O` is the nonnegative owner vector of the other `2q-1` owners in
the fibre.  Let `P` be the point-degree projection from owner vectors to
`Z^[k]`.

### Lemma 1.1 (period-`2q` auxiliary congruence)

For every such fibre,

\[
 P a_O\equiv-\mathbf 1_O\pmod q                 \tag{1.2}
\]

coordinatewise.

### Proof

Every core coordinate occurs in all `2q` owners of the full rail, and
every active coordinate occurs in exactly `q` cyclic `q`-windows.  Hence

\[
 P f_O=2q\,\mathbf 1_{C_O}+q\,\mathbf 1_{T_O}
       \equiv0\pmod q.                             \tag{1.3}
\]

Since `a_O=f_O-e_O`, (1.2) follows.  No disjointness, order, or choice of
tag set is used.  \(\square\)

The lemma remains true if the fibres use different cores, active sets,
orders, graph signatures, or fresh-label sets.

## 2. No singleton recovery for the conformal macro

Let `B^+` and `B^-` be finite simple rank-`R` owner families satisfying

\[
 P\mathbf 1_{B^+}=P\mathbf 1_{B^-}.                \tag{2.1}
\]

This is exactly the point-degree equality proved for the two boundary
shores of the insertion--star conformal macro.  Suppose a period-`2q`
fibre `F_O` containing `O` is chosen for every owner in
`B^+ union B^- union {H}`.

### Theorem 2.1 (scalar and mod-`q` singleton-recovery no-go)

The auxiliary-current equation

\[
 \sum_{O\in B^+}a_O-
 \sum_{O\in B^-}a_O=a_H                          \tag{2.2}
\]

is impossible.

### Proof

There is already a scalar obstruction.  Taking the sum of the point-degree
coordinates in (2.1) gives

\[
 R|B^+|=R|B^-|,
\]

so `|B^+|=|B^-|`.  Every `a_O` contains exactly `2q-1` owners.  The total
owner coefficient on the left of (2.2) is therefore zero, while that on
the right is `2q-1`.

The coordinatewise obstruction is stronger and records what remains even
if one later appends scalar-neutral auxiliary trades.  Apply `P` and reduce
modulo `q`.  Lemma 1.1 and (2.1) give

\[
 P\left(\sum_{B^+}a_O-\sum_{B^-}a_O\right)
 \equiv
 -P\mathbf1_{B^+}+P\mathbf1_{B^-}
 \equiv0\pmod q.                                  \tag{2.3}
\]

But

\[
 Pa_H\equiv-\mathbf1_H\not\equiv0\pmod q,        \tag{2.4}
\]

because `H` is nonempty and `q >= 2`.  This contradicts (2.2).
\(\square\)

Now write the original owner-current identity as

\[
 B^+-B^-=e_H-Y_H.                                 \tag{2.5}
\]

Replacing `e_O` by `f_O=e_O+a_O` would turn (2.5) into the desired
mixed identity

\[
 \sum_{B^+}f_O-\sum_{B^-}f_O=f_H-Y_H              \tag{2.6}
\]

if and only if (2.2) held.  Therefore (2.6) is impossible for arbitrary
period-`2q` pure-rail fibres, even before owner, palette, socket, or cap
collisions are considered.

This is stronger than a failure of a particular graph/tag packing.  It
rules out every attempt which keeps the original macro current `Y_H` and
tries to convert just its named boundary owners and `H` into period-`2q`
fibres.

## 3. What full inflation does preserve

There is no contradiction in applying a formal fibre map to **every**
owner basis vector in (2.5), including all owner occurrences used to
represent `Y_H`.  On the free owner module, linearity gives

\[
 \mathfrak F(B^+)-\mathfrak F(B^-)
 =f_H-\mathfrak F(Y_H).                            \tag{3.1}
\]

Provided the chosen fibre supports are physically disjoint, every term
in (3.1) is a signed union of complete legal rails.  But (3.1) is a
**fully inflated** identity: the residual is the whole rail `f_H`, and
the original macro has been replaced by its ownerwise inflation
`F(Y_H)`.  It does not recover `e_H`, and it does not preserve the
original compulsory-ticket current without an additional compatibility
theorem.

In particular, merely assigning pairwise-disjoint graph or tag signatures
cannot evade Theorem 2.1.  Such signatures may solve owner collisions;
they do not change (1.2).

## 4. Strongest unconditional structured-leave theorem

The companion complementary-fibre theorem proves the following exact
semigroup statement.  If graph edge families satisfy

\[
 F_1=F_0\sqcup\{h\},                              \tag{4.1}
\]

then, under `R >= 3q` and `k-R >= q+2`, their vertical fibre lifts satisfy

\[
 \mathcal B(F_1)=\mathcal B(F_0)\sqcup\mathcal B(h), \tag{4.2}
\]

where `B(h)` is one legal owner-simple, proper-deck-simple, biresident
period-`2q` rail.  Thus the graph star--cycle absorber converts a singleton
graph-edge residue into one **whole-rail** residue exactly.

Consequently a downstream theorem can use this construction without any
loss of rigor if its terminal defect class consists of a bounded number
of complete fibres `B(h)`.  Such a theorem must explicitly prove both:

1. the global cover-down leave is a union of at most `O(1)` compatible
   complete fibres; and
2. one complete fibre costs `O(1)` terminal compiler letters or can be
   spliced into an existing component at `O(1)` cost.

Under those two hypotheses the contribution is `O(1)`, independent of
the `2q` owners inside each fibre.  Without them, counting the fibre as
one defect is not justified.

## 5. Exact escape routes

The obstruction uses only the facts that the full rail has period
divisible by `q` and every active point has degree `q`.  Possible escape
routes must therefore change at least one premise.  Examples are:

* use non-`0 mod q` periods and solve the resulting core/window current;
* use a coupled compound gadget which is not a disjoint sum of one fibre
  per boundary owner;
* allow a class-changing terminal component and retain a whole-rail
  structured leave; or
* inflate the entire macro and accept that both `Y_H` and `H` have been
  replaced by their fibre images.

No period-`2q` source-fibre packing, however sophisticated, can by itself
turn the existing `B^+-B^-` conformal identity back into a singleton
`H` identity.

## 6. Exact current for a variable-period fibre

The companion lift works more generally at every period `m >= 2q`.
Write a source owner as

\[
 O=C_O\sqcup W_O,
 \qquad |C_O|=R-q,\quad |W_O|=q,
\]

and let the active set be `T_O=W_O \sqcup Z_O`, of size `m`.  Removing the
source owner from its period-`m` rail gives

\[
 P a_O
 =(m-1)\mathbf1_{C_O}
 +(q-1)\mathbf1_{W_O}
 +q\mathbf1_{Z_O}.                                 \tag{6.1}
\]

If `delta=m-2q`, reduction modulo `q` gives

\[
 P a_O
 \equiv(\delta-1)\mathbf1_{C_O}-\mathbf1_{W_O}
 \pmod q.                                          \tag{6.2}
\]

Thus the period-`2q` class is `-1_O`, while

\[
 m=2q+1:\quad Pa_O\equiv-\mathbf1_{W_O}\pmod q,   \tag{6.3}
\]

\[
 m=2q+2:\quad Pa_O\equiv
 \mathbf1_{C_O}-\mathbf1_{W_O}\pmod q.             \tag{6.4}
\]

The total auxiliary owner count is

\[
 \mathbf1^Ta_O=m-1.                                \tag{6.5}
\]

Therefore a variable-period compound inflation is not covered by Theorem
2.1.  It must solve, simultaneously, the scalar ledger

\[
 \sum_{B^+}(m_O-1)-\sum_{B^-}(m_O-1)=m_H-1         \tag{6.6}
\]

and the coordinate ledger obtained from (6.1).  Equations (6.1)--(6.6)
are an exact finite reduction for that escape route.  In particular,
period `2q+1` fibres can change the mod-`q` core class which was frozen in
the uniform period-`2q` construction.  No compatible choice satisfying
the full ledgers is proved here.

## 7. Edgewise clock insertion does not repair the explicit period-`2q` graph lift

There is a second natural attempt.  Keep the period-`2q` residual fibre
over the missing graph edge `h=uv`, and on each common graph edge
`e in G=S-uv` allow a signed insertion which lengthens its active clock by
one point.  An insertion pair has exact owner point current

\[
 P(F_e^+-F_e^-)=\mathbf1_{C_e}+q e_{z_e},          \tag{7.1}
\]

where, even if the removed `q`-set in `D` is allowed to depend on `e`,

\[
 C_e=(D\setminus W_e)\cup(V\setminus e).           \tag{7.2}
\]

Allow arbitrary signed integer multiplicities `s_e`.  Suppose these
insertions could collapse the whole residual fibre to its distinguished
owner:

\[
 f_{uv}+\sum_{e\in G}s_e(F_e^+-F_e^-)=e_H.         \tag{7.3}
\]

The total-owner-count row of (7.3) gives

\[
 \sum_{e\in G}s_e=1-2q\equiv1\pmod q.             \tag{7.4}
\]

Put `S_0=sum_e s_e` and define the signed graph degree

\[
 d_s(x)=\sum_{e\in G:x\in e}s_e.
\]

The full period-`2q` fibre has point current zero modulo `q`, and the
`q e_{z_e}` terms in (7.1) also vanish.  On a coordinate `x in V`, the
coefficient of `sum_e s_e 1_{C_e}` is

\[
 S_0-d_s(x).                                       \tag{7.5}
\]

Since `H=D union L` and `V=L sqcup {u,v}`, equations (7.3)--(7.5) force

\[
 d_s(l)=0\quad(l\in L),\qquad
 d_s(u)=d_s(v)=1                                  \tag{7.6}
\]

modulo `q`.

These equations are impossible in both explicit graph absorbers.

* For odd `q`, the vertex `v` is isolated in `G=S-uv`, contradicting
  `d_s(v)=1`.
* For even `q`, `G=K_{A,B_0 union {u,v}}` and `A subset L`.  Summing
  `d_s(a)=0` over `a in A` counts every weighted edge once and gives
  `S_0=0`, contradicting (7.4).

Hence arbitrary signed edgewise one-point clock insertions cannot turn the
explicit period-`2q` whole-rail lift back into a singleton.  This statement
allows repetitions and ignores nonnegativity, so a literal packed version
is also impossible.

For a residual period `m`, the same calculation instead requires

\[
 d_s(l)=0\quad(l\in L),\qquad
 d_s(u)=d_s(v)=1-m\pmod q.                         \tag{7.7}
\]

Thus `m=2q+1` makes the right side zero and is not excluded by this graph
incidence invariant.  The longer-period escape identified in Section 6 is
therefore genuine rather than cosmetic.
