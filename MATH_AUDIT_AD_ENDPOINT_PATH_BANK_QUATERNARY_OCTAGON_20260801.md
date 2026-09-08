# Adversarial audit of the quaternary one-path cycle absorber

Date: 2026-08-01  
Audited source:
`MATH_THEOREM_AD_ENDPOINT_PATH_BANK_QUATERNARY_OCTAGON_20260801.md`  
Audited source SHA-256 after the private-rail and fixed-`H` scope patch:
`211b14e56128ace9de555b5711c885cdc3ac7c878c76e89af1d941a61b4c67a9`.  
Status: core four-resource identity, minimum-support theorem, topology order,
and even/odd completion counts are **sound**.  The fixed-`H` interface needs
one explicit topology/orientation scope correction recorded in Section 6.
The proposed quaternary-private shortest rail is also proved here at its
exact local scope.

## 1. Independent resource replay

Use the source notation

\[
\begin{aligned}
 L_i&=S+a_i,& U_i&=S+z+a_i+a_{i+1},\\
 A_i&=S+z+a_i,& B_i&=S+a_i+a_{i+1},
\end{aligned}                                             \tag{1.1}
\]

with indices modulo four.  The old and new atoms are

\[
                  o_i=A_i\to B_i,qquad n_i=A_i\to B_{i-1}.
                                                               \tag{1.2}
\]

Directly,

\[
\begin{array}{c|c|c}
 &\text{intersection}&\text{union}\\ \hline
o_i&S+a_i&S+z+a_i+a_{i+1}\\
n_i&S+a_i&S+z+a_{i-1}+a_i.
\end{array}                                               \tag{1.3}
\]

Thus the lower rows agree indexwise, the upper row is shifted by one, the
tail row is unchanged, and the head row is shifted by one.  All labels in
`S,z,a_0,a_1,a_2,a_3` have the required distinctness, so all four rows are
injective.  The alternating union graph has old edges `A_iB_i` and new
edges `A_(i+1)B_i`, hence is exactly

\[
 A_0-B_0-A_1-B_1-A_2-B_2-A_3-B_3-A_0.                  \tag{1.4}
\]

No hidden multiplicity or orientation issue occurs in the local identity.

## 2. Topology order

Assume `o_0` lies on a directed cycle and the old path edges occur in order

\[
                              o_1, o_3, o_2.            \tag{2.1}
\]

After deletion, denote the cycle return by `B_0 ==> A_0` and the path
fragments by

\[
 \mathrm{src}\Rightarrow A_1,quad
 B_1\Rightarrow A_3,quad
 B_3\Rightarrow A_2,quad
 B_2\Rightarrow\mathrm{snk}.                             \tag{2.2}
\]

The new arcs are

\[
 A_1\to B_0,quad A_0\to B_3,quad
 A_2\to B_1,quad A_3\to B_2.                            \tag{2.3}
\]

They concatenate the fragments uniquely as

\[
\begin{split}
 \mathrm{src}\Rightarrow A_1\to B_0
 \Rightarrow A_0\to B_3
 \Rightarrow A_2\to B_1
 \Rightarrow A_3\to B_2
 \Rightarrow\mathrm{snk}.
\end{split}                                               \tag{2.4}
\]

This is one path and contains no cycle.  Therefore Theorem 4.1's unusual
order `1,3,2` is correct; replacing it by the numeric order `1,2,3` would
not prove the stated concatenation.

## 3. Support-three lower bound

Equality of typed tail and head multisets makes every exact support-`s`
phase a permutation of the `s` old head ports among the old tail ports.  A
fixed point is the identical old atom; after deleting it, the remaining
atoms still form an exact exchange.  The audited Boolean-square theorem
rules out a nontrivial support-two exchange.  Hence every nonidentity
support-three phase has a head permutation which is a 3-cycle.

For one cycle cut and two ordered path cuts, one orientation of this
3-cycle joins the opened cycle return to the intervening path fragment and
closes them; the other closes the intervening path fragment itself.  For
two cycle cuts and one path cut, the two orientations close respectively
one of the two cycle fragments.  Thus a cycle remains in every possible
support-three phase.

There is one minor proof-detail worth stating.  If two selected cuts are
adjacent, one displayed fragment can have length zero.  The purported new
arc which would "close" that fragment is then a forbidden loop, so that
orientation is not a legal Johnson phase; the other orientation still
closes the other nonempty fragment.  Therefore adjacency does not create a
counterexample, but the source proof should read zero-length cases in this
way rather than regarding a loop as a directed cycle.

The support-four octagon is consequently minimum for the class "one old
cycle component plus one old path component".  This does not assert that
every such component pair contains an applicable octagon.

## 4. Even/odd menu counts

Fix the complete oriented target `o_0`, not merely its outer colours.
Choosing `a_0 in L_0` fixes `S=L_0-a_0`; the target orientation fixes

\[
                    z=A_0-L_0,qquad a_1=B_0-L_0.        \tag{4.1}
\]

The remaining ordered pair `(a_2,a_3)` lies outside `U_0`.

* On a `2m`-point ground set, `|Omega-U_0|=m-1`, giving

  \[
                 (m-1)(m-1)(m-2)=(m-1)^2(m-2).          \tag{4.2}
  \]

* On a `(2m-1)`-point ground set, `|Omega-U_0|=m-2`, giving

  \[
                 (m-1)(m-2)(m-3).                       \tag{4.3}
  \]

Both source counts are exact.  The odd construction first exists at
`m=4`, exactly when `(2m-1)>=(m-2)+5`.

## 5. Quaternary-private shortest resident rail

There is a useful explicit strengthening of the source's conditional rail
interface.  Regard

\[
 o_0:A_0\to B_0
\quad\text{as}\quad
 E=L+d_0\to F=L+a                               \tag{5.1}
\]

by setting

\[
 L=L_0=S+a_0,qquad d_0=z,qquad a=a_1.                 \tag{5.2}
\]

Choose distinct

\[
 x_0,\ldots,x_{h-1}\in S,qquad
 y\notin U_0\cup\{a_2,a_3\}.                            \tag{5.3}
\]

Put

\[
 Z=L+a+d_0+y=S+a_0+a_1+z+y                              \tag{5.4}
\]

and take the rotating-hole order

\[
          (z_0,z_1,z_2,z_3,\ldots,z_{h+2})
          =(a_1,y,z,x_0,\ldots,x_{h-1}),                 \tag{5.5}
\]

with `V_i=Z-{z_i,z_(i+1)}` cyclically.  Then `V_0=A_0`,
`V_1=B_0`, and

\[
                   B_0=V_1\to V_2\to\cdots
                       \to V_{h+2}\to V_0=A_0           \tag{5.6}
\]

is a shortest depth-`h` resident return rail.

### Theorem 5.1 (exact quaternary privacy and local residence)

Every return-rail upper colour contains `y`, whereas no quaternary upper
colour `U_i` contains `y`.  Among the return-rail lower colours, the only
one containing neither `y` nor `z` is

\[
                         L-x_0+a_1
                       =S-x_0+a_0+a_1,                   \tag{5.7}
\]

and it differs from every `L_i=S+a_i`.  All internal return vertices
contain `y`, while none of the eight octagon vertices does.  Hence the
return rail is fully four-resource-private from the quaternary packet away
from its intended endpoints.

Moreover the local new fragment

\[
              A_1,B_0,V_2,\ldots,V_{h+2},A_0,B_3        \tag{5.8}
\]

has no internal positive coordinate run shorter than `h+1`.

#### Proof

The rotating-hole formulas give return upper colours

\[
                         u_i=Z-z_{i+1}                   \tag{5.9}
\]

for `1<=i<=h+2`.  None deletes `z_1=y`, proving the upper
claim.  Its lower colours are

\[
                         ell_i=Z-\{z_i,z_{i+1},z_{i+2}\}.
                                                               \tag{5.10}
\]

The first return edge deletes `y,z,x_0` and gives (5.7).  A later return
lower either retains `y`, or (at the wrap end) deletes `y` but retains `z`.
Formula (5.7) contains both `a_0,a_1` and omits `x_0 in S`, so it cannot be
any `S+a_i`.  Internal return vertices omit two labels other than `y` and
therefore contain `y`, proving physical privacy.

For residence, `y` occurs on exactly `V_2,...,V_(h+2)`, an internal run of
length `h+1`.  Coordinate `z` has a left endpoint singleton at `A_1` and an
internal run of length `h+1` ending at `A_0`.  Coordinate `a_1` has only a
left-clipped run; `a_0` has only a right-clipped run.  Every `x_j` is absent
at two consecutive rail vertices and is present at both external ends, so
its two positive pieces are endpoint-clipped.  Coordinate `a_3` occurs
only at the right endpoint, and `a_2` is absent.  Every remaining
coordinate is constant.  This proves (5.8).  \(\square\)

The exact number of choices after the quaternary packet is fixed is

\[
\begin{array}{c|c}
|\Omega|&\text{rail count}\\ \hline
2m&(m-3)(m-2)_h,\\
2m-1&(m-4)(m-2)_h.
\end{array}                                               \tag{5.11}
\]

Indeed `S` supplies `(m-2)_h` ordered `x`-tuples; outside `U_0` there are
respectively `m-1` and `m-2` labels, of which `a_2,a_3` are excluded.
These counts require the displayed factors to be positive.  The theorem
asserts residence only for the old target cycle and for the local fragment
(5.8).  It does not certify the two other octagon joins or a globally
ordered OR word.

## 6. Fixed-`H` interface: exact correction

The source is correct that a prepared 2-bounded incidence skeleton with at
most `m-2` incidence edges extends to an undirected spanning q1 two-factor.
It is also correct that the local octagon toggle preserves every resource
it touches.

Two statements do **not** follow from that extension theorem alone.

1. A protected path skeleton ceases to be a path **component** after its
   two endpoints are completed to degree two.  Therefore Theorem 4.1's
   one-cycle-plus-one-path topology conclusion need not survive an
   arbitrary two-factor completion.  The exact post-completion condition is
   the relative graphic-rank inequality

   \[
                      r_K(N)>r_K(O),                     \tag{6.1}
   \]

   after contracting the unchanged completion `K`; for a one-cycle drop
   the gain must be exactly one.

2. An undirected q1 completion does not automatically orient every one of
   several protected path fragments in their prescribed directions.  If
   multiple protected fragments land on one completed component, their
   requested orientations can conflict.  A directed/rooted extension or a
   separate orientation-consistency condition is needed for the full typed
   tail/head interpretation.

Thus the fixed-`H` theorem supplies an unconditional q1/cap-two **embedding
of the skeleton**, not an unconditional global cycle absorber.  A prepared
literal path component, or a rooted completion satisfying (6.1) and the
orientation constraints, restores the exact topology theorem.  The source
already disclaims global upper completion; this audit adds the equally
necessary rooted-topology qualification.

## 7. Formatting-only source corrections

The source had three harmless TeX omissions which did not affect the proof:

* close the display after source equation `(3.9)`;
* replace `quad` by `\quad` twice in `(4.4)`; and
* close the display after `(4.4)`.

All three have been applied in the source.

## 8. Verdict

The exact local result survives adversarial audit:

\[
\boxed{\text{one cycle + one compatible path admits a minimum-support}
       \ 4\leftrightarrow4\ \text{absorber}.}
\]

The fixed target has exactly the menu sizes (4.2)--(4.3), and the explicit
rail has exactly the private counts (5.11).  The arbitrary-component supply,
rooted directed completion, global upper row, exterior residence, deeper
OR shadows and common cap remain separate.
