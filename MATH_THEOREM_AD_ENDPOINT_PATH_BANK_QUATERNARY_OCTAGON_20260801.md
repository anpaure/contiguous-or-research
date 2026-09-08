# A quaternary Boolean octagon is the minimum one-path cycle absorber

Date: 2026-08-01  
Lane: AD, endpoint-bearing replacement for the cycle-internal no-go  
Status: exact central four-resource and physical-topology theorem.  No
OR-word, residence-at-exterior-joins, deep-shadow, common-cap, or global
upper-factor statement is claimed.

## 0. Outcome

Exact lower/upper/tail/head balance cannot destroy a directed cycle using
only atoms of that cycle.  Importing an endpoint-bearing path is sufficient,
and the exact minimum support depends on how many path components are
available.

* With two distinct path components, the ternary Boolean hexagon is a
  `3 <-> 3` exchange: one cycle edge and one edge from each path become two
  paths.  Support three is minimum.
* With only one path component, no exchange of support at most three can
  remove the cycle.  There is, however, an explicit `4 <-> 4` Boolean
  octagon which takes one edge from the cycle and three ordered edges from
  the path and merges the two components into one path.  Hence support four
  is necessary and sufficient.

The `4 <-> 4` identity preserves the two outer palettes and both typed
middle banks literally.  Consequently it preserves indegree and outdegree
at every physical owner and therefore preserves the cap-two condition in
every ambient four-resource factor.

This is the sharp central answer.  The shortest resident return rail may be
kept as the unchanged return segment around the distinguished cycle edge,
and the fixed-`H` q1 two-factor extension theorem may embed a separately
prepared bounded protected path/cycle skeleton.  Neither result supplies
global adjacent-upper surjectivity, exterior residence at the joins, deep
OR witnesses, or one common compiler.

## 1. Port normal form for an exact exchange

An ordered Boolean-diamond atom is

\[
                 e=(L(e),U(e),T(e),H(e)),
\tag{1.1}
\]

where `T(e)` and `H(e)` are adjacent rank-`m` sets and

\[
                 L(e)=T(e)\cap H(e),\qquad
                 U(e)=T(e)\cup H(e).
\tag{1.2}
\]

Let `O={e_0,...,e_(s-1)}` and `N` be two four-resource matchings with the
same four typed resource multisets.  Since the old tails are distinct, index
the new atoms by their tails.  There is then a unique permutation
`sigma in S_s` such that the new atom with tail `T(e_i)` has head
`H(e_(sigma(i)))`.

### Lemma 1.1 (successor-permutation normal form)

The physical part of every exact exchange is obtained by permuting the old
head ports among the old tail ports.  If `sigma(i)=i`, then the corresponding
new atom is exactly `e_i`.  In particular, if `sigma` fixes all but two
indices, the remaining two atoms form a nontrivial exact `2 <-> 2`
four-resource exchange.

#### Proof

Equality of the typed tail and head multisets gives the permutation.  A
tail/head pair determines its lower intersection and upper union uniquely,
so a fixed physical arc determines the complete ordered atom.  Removing a
fixed atom from the four multiset equalities leaves the four equalities on
the remaining atoms.  \(\square\)

We use the proved Boolean-diamond square obstruction: a nontrivial exact
`2 <-> 2` exchange does not exist.  It follows that a nonidentity exchange
on three atoms has successor permutation a 3-cycle.

## 2. Why one path cannot work at support three

Let an ambient directed cap-two factor consist of directed path and directed
cycle components.  Cutting an old arc `t -> h` exposes an outgoing port `t`
and an incoming port `h`.  An uncut directed fragment is denoted
`h ==> t`.

### Theorem 2.1 (one-path support-three obstruction)

Suppose an exact exchange of support at most three is contained in the union
of one directed-cycle component `C` and one directed-path component `P`, and
suppose it uses at least one old atom from each component.  Its new physical
graph still contains a directed cycle.

#### Proof

Supports one and two are trivial by Lemma 1.1 and the Boolean square
obstruction.  At support three the successor permutation is a 3-cycle.
There are two cases.

**One cycle cut and two path cuts.**  Call the cycle cut `c`, and call the
two path cuts `p,q` in their directed order.  After deletion there are
fragments

\[
                    h_c\Longrightarrow t_c,
              \qquad h_p\Longrightarrow t_q.
\tag{2.1}
\]

Up to reversing the 3-cycle, the two head permutations are

\[
 c\mapsto p,\ p\mapsto q,\ q\mapsto c
 \quad\hbox{or}\quad
 c\mapsto q,\ q\mapsto p,\ p\mapsto c.
\tag{2.2}
\]

In the first case, the new arcs `t_c -> h_p` and `t_q -> h_c`, together
with the two fragments in (2.1), form a directed cycle.  In the second case,
the new arc `t_q -> h_p` closes the middle path fragment by itself.
If the two path cuts are adjacent, that middle fragment has length zero and
the latter arc would be a forbidden loop, so that orientation is not a legal
Johnson phase; the first orientation still closes the nonzero combined
fragment.

**Two cycle cuts and one path cut.**  Call the cycle cuts `c,p` in cyclic
order.  The two cycle fragments are

\[
                    h_c\Longrightarrow t_p,
              \qquad h_p\Longrightarrow t_c.
\tag{2.3}
\]

One orientation of the 3-cycle inserts `t_c -> h_p` and closes the second
fragment; the other inserts `t_p -> h_c` and closes the first.
If one cycle fragment has length zero, the corresponding closing arc is a
forbidden loop and the other orientation still closes the complementary
nonzero fragment.

Thus every genuine support-three permutation leaves a cycle.  \(\square\)

This is purely a port obstruction once the nonexistence of a Boolean
`2 <-> 2` exchange is known.  It does not depend on a particular local
packet catalogue.

### Corollary 2.2 (two paths are exactly what the ternary packet pays)

If the two noncycle old atoms lie on two distinct path components, the
ternary Boolean-hex exchange removes one cycle and returns two paths.  Thus
two path components need support exactly three, while one path component
needs support at least four.

The positive assertion is the literal ternary identity in
`MATH_THEOREM_BOOLEAN_HEX_TERNARY_FOUR_RESOURCE_ABSORBER_20260801.md`;
Theorem 2.1 explains why its two separate endpoint banks cannot simply be
identified at support three.

## 3. The quaternary outer octagon

Assume `m>=3` and that the ground set has at least `m+3` labels.  Let `S`
have size `m-2`, and choose five distinct labels

\[
                         z,a_0,a_1,a_2,a_3
\tag{3.1}
\]

outside `S`.  Indices are modulo four.  Put

\[
\begin{aligned}
 L_i&=S\cup\{a_i\},
 &U_i&=S\cup\{z,a_i,a_{i+1}\},\\
 A_i&=S\cup\{z,a_i\},
 &B_i&=S\cup\{a_i,a_{i+1}\}.
\end{aligned}
\tag{3.2}
\]

Define the old and new atoms

\[
 o_i=(L_i,U_i,A_i,B_i),
 \qquad
 n_i=(L_i,U_{i-1},A_i,B_{i-1}),
\tag{3.3}
\]

and set

\[
                         O=\{o_0,o_1,o_2,o_3\},
             \qquad      N=\{n_0,n_1,n_2,n_3\}.
\tag{3.4}
\]

### Theorem 3.1 (exact quaternary four-resource identity)

Every atom in (3.3) is a legal ordered Boolean diamond.  Both `O` and `N`
are four-resource matchings, and their four typed resource sets agree:

\[
\begin{array}{c|c|c|c|c}
 &\text{lower}&\text{upper}&\text{tail}&\text{head}\\ \hline
 O&\{L_i\}&\{U_i\}&\{A_i\}&\{B_i\}\\
 N&\{L_i\}&\{U_{i-1}\}&\{A_i\}&\{B_{i-1}\}.
\end{array}
\tag{3.5}
\]

The union of their undirected physical projections is the alternating
octagon

\[
 A_0-B_0-A_1-B_1-A_2-B_2-A_3-B_3-A_0.
\tag{3.6}
\]

#### Proof

For an old atom,

\[
 A_i\cap B_i=S+a_i=L_i,
 \qquad
 A_i\cup B_i=S+z+a_i+a_{i+1}=U_i.
\tag{3.7}
\]

For a new atom,

\[
 A_i\cap B_{i-1}=S+a_i=L_i,
 \qquad
 A_i\cup B_{i-1}=S+z+a_{i-1}+a_i=U_{i-1}.
\tag{3.8}
\]

The four `L_i`, four `U_i`, four `A_i`, and four `B_i` are separately
distinct.  This proves legality, injectivity and (3.5).  Formula (3.6)
follows from the old edges `A_iB_i` and the new edges `A_(i+1)B_i`.
\(\square\)

On the even ground set of size `2m`, one fixed oriented target `o_0` has

\[
                         (m-1)^2(m-2)
\tag{3.9}
\]

indexed completions of this displayed form: choose `a_0 in L_0`, which
fixes `S`; the orientation of `o_0` fixes `z,a_1`; then choose the ordered
pair `(a_2,a_3)` outside `U_0`.  This is a menu count only.  It does not say
that the other three old atoms occur on one path in the required order.

On the odd ground set of size `2m-1`, the same construction is available
for `m>=4` and the corresponding count is

\[
                         (m-1)(m-2)(m-3).
\tag{3.10}
\]

The difference is solely the size of the complement of `U_0`.

## 4. One cycle plus one path becomes one path

### Theorem 4.1 (minimum one-path absorber)

Let `G` be a directed graph of maximum indegree and outdegree at most one
whose arcs carry a four-resource matching.  Suppose `O subset G` and:

1. `o_0=A_0->B_0` lies on a directed cycle `C`;
2. `o_1=A_1->B_1`, `o_3=A_3->B_3`, and
   `o_2=A_2->B_2` occur in this directed order on one directed path `P`;
3. `C` and `P` are distinct components.

Then

\[
                           G'=(G-O)\cup N
\tag{4.1}
\]

has exactly the same lower, upper, tail and head resources as `G`, has the
same cap-two degrees, and replaces `C union P` by one directed path.  No
other component changes.  Consequently the cycle count drops by one.
In particular, an ambient factor which is complete on both outer shores
remains complete on both outer shores after the toggle.

Together with Theorem 2.1, support four is the exact minimum for an
absorber importing endpoints from only one path component.

#### Proof

Delete the four old arcs.  Write the resulting directed fragments as

\[
\begin{aligned}
 C_0&: B_0\Longrightarrow A_0,\\
 P_0&:\operatorname{src}(P)\Longrightarrow A_1,\\
 P_1&:B_1\Longrightarrow A_3,\\
 P_2&:B_3\Longrightarrow A_2,\\
 P_3&:B_2\Longrightarrow\operatorname{snk}(P).
\end{aligned}
\tag{4.2}
\]

The four new arcs concatenate them in the single order

\[
 P_0, n_1, C_0, n_0, P_2, n_2, P_1, n_3, P_3,
\tag{4.3}
\]

because

\[
 n_1=A_1B_0,\quad n_0=A_0B_3,\quad
 n_2=A_2B_1,\quad n_3=A_3B_2.
\tag{4.4}
\]

Thus (4.3) is one directed path and no cycle is created.  Theorem 3.1 gives
the exact four-resource equality.  In particular the selected tail set and
head set do not change, so every physical vertex retains its indegree and
outdegree contribution from the exchanged support.  The ambient degree cap
is therefore automatic.  Minimality is Theorem 2.1.  \(\square\)

### Corollary 4.2 (fixed private bank)

Let `H` be fixed.  If `H` quaternary packet supports are four-resource
disjoint and their `H` cycle/path component pairs are mutually disjoint,
then all `H` toggles commute.  They remove all `H` named cycles, preserve
all four central resource banks, and preserve cap two.

This is a prepared-bank theorem.  It does not prove that an arbitrary
four-resource factor contains the required ordered triples on its path
components.

## 5. Interface with the new rail and fixed-`H` q1 extension

Theorem 4.1 is compatible with the exact cycle-side return rail.  Take
`o_0=A_0->B_0` as the distinguished edge and adjoin any four-resource-private
directed return path from `B_0` to `A_0`.  The return path is unchanged by
the toggle.  It is exactly the fragment `C_0` in (4.2), so the proof remains
literal.  In particular the shortest resident return rail from
`MATH_THEOREM_BOOLEAN_HEX_SHORTEST_RESIDENT_RETURN_RAIL_AND_PHASE_DECOUPLING_20260801.md`
may be used whenever its non-target resources are private from the
quaternary packet.

That privacy can be realized explicitly.  In the notation of Section 3,
regard `o_0` as the target with

\[
 L=L_0=S+a_0,\qquad d_0=z,\qquad a=a_1.
\tag{5.1}
\]

Choose distinct `x_0,...,x_(h-1)` in `S` and choose

\[
                  y\notin U_0\cup\{a_2,a_3\}.
\tag{5.2}
\]

Put `Z=L+a_1+z+y`, take the cyclic label order

\[
              (a_1,y,z,x_0,\ldots,x_{h-1}),
\tag{5.3}
\]

and use the rotating-hole vertices `V_i=Z-{z_i,z_(i+1)}`.  The return path
is `B_0=V_1 -> V_2 -> ... -> V_(h+2) -> V_0=A_0`.

### Lemma 5.1 (quaternary-private shortest resident rail)

Whenever the choice (5.2) exists (in particular, `m>=4` on even ground and
`m>=5` on odd ground), and `1<=h<=m-2`, the displayed return path is
four-resource-private from
the other seven octagon atoms.  In the old phase it closes `o_0` into a
cycle whose every nonconstant positive run has length `h+1`.  In the new
phase its nontrivial local component is

\[
             A_1\to B_0\;R\;A_0\to B_3,
\tag{5.4}
\]

and it has no internal positive run shorter than `h+1`; the other two new
atoms are isolated path edges.  Thus both local phases are resident, while
exterior joins remain separate guards.

For one fixed quaternary packet the number of these rails is
`(m-3)(m-2)_h` on a `2m`-point ground set and
`(m-4)(m-2)_h` on a `(2m-1)`-point ground set.

#### Proof

The rotating-hole theorem gives Johnson legality, distinct rail palettes,
the run length on the old cycle, and shortest possible return length
`h+2`.  Every return-rail upper colour contains `y`, whereas no octagon
upper colour does.  Among return-rail lower colours, all but two contain
`y`; the two exceptions are

\[
                  L-x_0+a_1,\qquad L-x_{h-1}+z.
\tag{5.5}
\]

The second contains `z`.  In the first, `x_0 in S` leaves both `a_0,a_1`
and omits one element of `S`, so it cannot equal any `L_i=S+a_i`.
Every internal rail owner contains `y`, while no octagon owner does.
This proves complete resource privacy.

For residence in (5.4), `y` has its internal rail run of length `h+1`;
`z` has a clipped singleton at `A_1` and an internal run of length `h+1`
ending at `A_0`; `a_1` has only a leading clipped run; `a_0` is present on
the whole rail and at `B_3`; every `x_j` has only endpoint-clipped pieces;
and `a_3` occurs only at the terminal endpoint `B_3`.  All other
coordinates are constant.  Hence no shorter internal run occurs.  Finally,
the ordered distinct `x`-tuple has `(m-2)_h` choices.  Outside
`U_0` there are `m-1` labels on even ground and `m-2` on odd ground; after
excluding `a_2,a_3`, the asserted counts follow. \(\square\)

Likewise, the protected q1 extension theorem in
`MATH_THEOREM_FIXED_H_COLLAR_Q1_TWO_FACTOR_AND_ROOTED_HOST_GATE_20260801.md`
extends any separately prepared maximum-degree-two skeleton of at most
`m-2` incidence edges **on its odd Middle Levels host** to a spanning q1
two-factor.  One collared quaternary phase has exactly

\[
                         4+(h+2)=h+6
\tag{5.6}
\]

directed Johnson atoms: four octagon atoms and `h+2` unchanged return-rail
atoms.  Its incidence lift therefore has exactly `2(h+6)` edges and maximum
degree two.  For pairwise incidence-private collars of depths `h_i`, the
fixed-`H` theorem applies under the exact inequality

\[
                    2\sum_{i=1}^{H}(h_i+6)\le m-2.
\tag{5.7}
\]

The quaternary construction itself exists on that odd host for `m>=4`, with
count (3.10).  Thus (5.7) holds eventually for fixed `H` and `h_i=o(m)`.

There are six exact qualifications.

1. The extension theorem does not itself construct the ordered one-path
   topology required in Theorem 4.1.  It embeds the plus-phase incidence
   paths; a rooted completion/opening certificate must still ensure that
   reverse toggling places `o_1,o_3,o_2` in that order on one path.
2. The completion is undirected.  If several protected directed fragments
   land on one component, their prescribed directions must agree with one
   of its two global orientations.  Ore--Ryser does not impose this.
3. A completed two-factor has no path components until opening edges are
   chosen.  Equivalently, after contracting the common completion `K`, the
   exact topology row is the relative graphic-rank gain
   `r_K(N)-r_K(O)=1`.
4. The theorem embeds one selected phase.  The local reverse toggle still
   gives another undirected q1 two-factor because lower incidences and owner
   degrees are preserved, but it does not by itself certify a directed
   four-resource factor or a global upper-surjective host.
5. It controls the lower/q1 incidence factor, not global adjacent-upper
   surjectivity.  The local quaternary toggle preserves every upper resource
   it touches, but arbitrary completion can still have upper holes.
6. Residence at the rail's internal vertices does not imply residence at
   the two exterior joins in (4.3).

Hence the central endpoint/topology gate is closed for a prepared bank, but
the OR-word guards remain separate.

## 6. Exact boundary

The proved implication is

\[
\begin{array}{c}
\text{one cycle edge + three suitably ordered edges of one path}\\
\text{in the quaternary Boolean-octagon resource fibre}\\
\Downarrow\\
\text{one path, identical lower/upper/tail/head banks, cap two}.
\end{array}
\tag{6.1}
\]

The following are not proved:

* every directed cycle in an arbitrary exact factor has such an ordered
  quaternary partner triple;
* fixed-`H` q1 extension supplies the upper-surjective completion;
* the new long path preserves exterior residence or deeper shadows; or
* either phase has a common-cap literal OR compiler.

Thus the smallest central packet is completely classified, while packet
supply and every OR-word guard remain genuine downstream conditions.

## 7. Replay and independent audits

Run

```text
python3 scratch/audit_ad_endpoint_path_bank_quaternary_octagon_20260801.py
```

The dependency-free replay checks the complete four-resource identity for
`3<=m<=10`, both support-three port permutations, the exact one-path
concatenation, all even-ground resident rails for `4<=m<=10`, and all
odd-ground resident rails for `5<=m<=10`.  It also checks the exact
`2(h+6)` incidence count.  The frozen output is
`scratch/ad_endpoint_path_bank_quaternary_octagon_20260801.audit.json` and
reports

```text
PASS_AD_ENDPOINT_PATH_BANK_QUATERNARY_OCTAGON
payload_sha256=ebc74fdc2b7fa2b169b0279682f31465773a2e20f12b75942aa56dcdb1403640
```

The proof and the fixed-`H` scope were independently audited in
`MATH_AUDIT_AD_ENDPOINT_PATH_BANK_QUATERNARY_OCTAGON_20260801.md` and
`MATH_AUDIT_AD_ENDPOINT_BEARING_PATH_BANK_ABSORBER_INTERFACE_20260801.md`.
