# Infinity-cut MSW at critical height: global rotor reduction and fixed-top no-go

Date: 2026-07-26

Method: pure mathematics. Imported inputs are the exact odd wreath factor,
the audited special-coordinate bridge lift, and the audited canonical MSW
depth-one hole bound.

## 0. Result

Put

\[
 Q=[2m],\quad W=\binom{2m}{m},\quad
 B=\operatorname {Cat}_m={W\over m+1},\quad
 H=(1+o(1))\sqrt{m\log m}.
\tag{0.1}
\]

Let \(F\) be an exact wreath factor on \(Q\cup\{\infty\}\). Cutting every
row at \(\infty\) gives \(B\) complementary Johnson paths which partition
\(\binom Qm\). Every path has a full radius-\(H\) bridge-one lift, so

\[
\boxed{p=B=o(W/H),\qquad W+2HB=W+o(W).}
\tag{0.2}
\]

Thus the odd factor is a genuinely global construction which evades the
block-factor obstruction for independently selected promotion rings.

It does **not** become a critical-top promotion factor by cutting. A
consecutive subpath with \(s\) middle owners has union size \(m+s-1\).
Containment in one top of size \(m+H\) forces \(s\le H+1\). Therefore any
conversion which only cuts the inherited paths into fixed-top pieces has

\[
\boxed{p_{\rm top}\ge {W\over H+1}
       =(1-o(1)){W\over H},\qquad
       2Hp_{\rm top}\ge(2-o(1))W.}
\tag{0.3}
\]

This is a statewise no-go at exactly the required little-\(o\) scale.
Any promotion-ring conversion must globally rethread different cut paths.

There is, however, a direct non-promotion route. At signed depth \(q\),
all but \(q\) flags at each end of every intact path are forced by its
middle chronology. If \(h_q^{-,\mathrm{int}}\) and
\(h_q^{+,\mathrm{int}}\) count targets missed by these forced flags, every
full bridge lift which covers the corresponding signed ranks must satisfy

\[
\boxed{h_q^{-,\mathrm{int}}\le qB,\qquad
       h_q^{+,\mathrm{int}}\le qB.}
\tag{0.4}
\]

The remaining choices are one nested lower terminal queue and one nested
upper initial queue per path. If these queues can cover every signed rank
through \(H\), (0.2) plus the audited exterior product-SCD word proves
coefficient one.

More generally, cutting the inherited owner paths into \(p\ge B\) pieces
creates at most \(qp\) adjustable flags of either sign at depth \(q\).
Hence every coefficient-one use with \(p=o(W/H)\) necessarily satisfies

\[
\boxed{h_1^{-,\mathrm{int}}+h_1^{+,\mathrm{int}}=o(W/H)}
\tag{0.4a}
\]

for the forced depth-one interiors (and separately
\(h_q^{\pm,\mathrm{int}}\le qp\)). This is substantially stronger than
an unquantified \(o(W)\) first-shadow estimate. Thus the intact-cut route
is genuinely global but pays for its small path count by a sharp shallow
endpoint-capacity requirement.

For the canonical MSW factor, the audited odd depth-one hole bound further
implies that at least

\[
\boxed{(1/8-o(1))m}
\tag{0.5}
\]

choices of deleted coordinate fail (0.4) already at \(q=1\). This is a
positive-density deletion obstruction, not a refutation of every
coordinate.

## 1. Exact owner paths and count comparison

Rotate one odd wreath so its omitted-label order is

\[
(\infty,a_0,\ldots,a_{m-1},b_0,\ldots,b_{m-1}).
\tag{1.1}
\]

Its \(m+1\) middle windows avoiding \(\infty\) are

\[
X_t=\{a_t,\ldots,a_{m-1},b_0,\ldots,b_{t-1}\},
\quad0\le t\le m,
\tag{1.2}
\]

and

\[
X_{t+1}=X_t-a_t+b_t,\qquad X_m=Q\setminus X_0.
\tag{1.3}
\]

Exact odd ownership makes all lists (1.2) disjoint and exhaustive; their
count is \((m+1)B=W\). With

\[
w=(a_0,\ldots,a_{m-1},b_0,\ldots,b_{m-1}),
\tag{1.4}
\]

we have \(X_t=I_w(t,m)\). The exact bridge lift in
MATH_ATTACK_W_SPECIAL_COORDINATE_PBBS_PATH_FLAGS_20260725.md works for
every \(H<m\), proving (0.2).

If \(N_H=\binom{2m}{m-H}\) is the critical top count and
\(\theta=(m+H)N_H/W=1+o(1)\), then

\[
{B\over N_H}={m+H\over(m+1)\theta}=1+O(H/m).
\tag{1.5}
\]

The two constructions therefore have asymptotically the same component
count, although their geometry differs.

## 2. Fixed-top slicing obstruction

For \(s\) consecutive owners in (1.2),

\[
\bigcup_{t=a}^{a+s-1}X_t=I_w(a,m+s-1),
\qquad
\left|\bigcup_{t=a}^{a+s-1}X_t\right|=m+s-1.
\tag{2.1}
\]

Every promotion-ring middle owner over a top \(U\) is a subset of that
fixed \(U\), with \(|U|=m+H\). Hence an unrethreaded path piece assigned
to one top has \(s\le H+1\). Partitioning all \(W\) owners into such
pieces gives (0.3). Collars and tags cannot change this middle-union
invariant.

## 3. Forced interior flags and the exact successor gate

At physical edge \(t\), bridge one changes the owner by deleting \(a_t\)
and inserting \(b_t\). The bridge classification forces \(a_t\) to be
the last lower marker. Iterating the queue recurrence gives, whenever
\(t+q\le m\),

\[
\boxed{L_q(X_t)=
X_t\setminus\{a_t,\ldots,a_{t+q-1}\}
=I_w(t+q,m-q).}
\tag{3.1}
\]

Thus only the last \(q\) lower flags in one path depend on its terminal
queue. Dually, after \(q\) transitions the initial upper queue is flushed,
and for \(t\ge q\),

\[
\boxed{U_q(X_t)=
X_t\cup\{a_{t-q},\ldots,a_{t-1}\}
=I_w(t-q,m+q).}
\tag{3.2}
\]

Only the first \(q\) upper flags are free. Across \(B\) paths there are
therefore at most \(qB\) adjustable flags at either sign. One adjustable
flag fills at most one forced hole, proving (0.4) as a necessary condition
for a covering lift.  An arbitrary noncovering bridge lift need not satisfy
(0.4).

If the \(B\) inherited paths are cut further into \(p\) pieces, the same
argument gives at most \(qp\) adjustable flags at either sign. The
literal collar ledger requires \(p=o(W/H)\), and the specialization
\(q=1\) proves (0.4a).

The lower choices are exactly the nested Ferrers terminal queues of
Proposition 7.1 in the special-coordinate note; the upper choices are
the analogous initial queues. Hence (0.4) is only the full-set capacity
cut. Proper Hall cuts and the requirement that one queue serve all depths
remain.

### Corollary 3.1 (global completion reduction)

Suppose an exact odd factor, one deleted coordinate, path orientations,
and legal endpoint queues can be chosen so that the resulting full flags
cover every target at ranks \(m\pm q\), \(1\le q\le H\). Their central
word has length \(W+2HB=W+o(W)\). Since \(H/\sqrt m\to\infty\) and
\(H=o(m)\), the audited product-SCD exterior costs \(o(W)\). Thus this
hypothesis implies coefficient one.

## 4. Canonical MSW: many coordinates fail depth one

Let \(\mathscr H\) be the canonical odd MSW depth-one hole set and
\(h=|\mathscr H|\). For a coordinate \(z\), put

\[
h_z=|\{S\in\mathscr H:z\notin S\}|.
\tag{4.1}
\]

Every \(S\in\mathscr H\) has size \(m-1\), so

\[
\sum_z h_z=(m+2)h.
\tag{4.2}
\]

After cutting at \(z\), all forced internal lower first flags are original
odd \((m-1)\)-intervals avoiding \(z\). Hence all \(h_z\) targets are
forced internal holes and only the \(B\) terminal flags can fill them:

\[
h_z>B\quad\Longrightarrow\quad
\text{no depth-one covering lift after deleting \(z\)}.
\tag{4.3}
\]

Let \(K=|\{z:h_z>B\}|\). Since
\(\binom{2m}{m-1}=mB\),

\[
(m+2)h\le K(mB)+(2m+1-K)B,
\tag{4.4}
\]

and therefore

\[
K\ge{(m+2)h-(2m+1)B\over(m-1)B}.
\tag{4.5}
\]

The audited bound

\[
h\ge(1/16-o(1))\binom{2m+1}{m},
\qquad
\binom{2m+1}{m}={2m+1\over m+1}W
\tag{4.6}
\]

turns (4.5) into \(K\ge(1/8-o(1))m\), proving (0.5).

Canonical MSW is not translation-invariant, so this averaging argument
does not extend the obstruction to every coordinate.

## 5. Boundary

Proved: exact even owner coverage, \(B=o(W/H)\) global paths, critical
literal overhead \(o(W)\), the fixed-top slicing no-go, the forced
interior flag formulas, and the positive-density canonical deletion
obstruction.

Open: one deletion coordinate passing all cuts (0.4), simultaneous nested
endpoint queues through critical \(H\), a different odd factor with this
property, or a genuinely global rethreading into critical fixed-top rings.

The most economical surviving target is to preserve the intact infinity-cut
rotor paths and solve their coupled endpoint-queue cover. It uses the full
global structure and is outside the scope of the local block theorem.
