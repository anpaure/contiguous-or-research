# Complete lag-two promotion packets cannot form a one-edge-per-task train

**Date:** 2026-08-07  
**Status:** unconditional cross-core no-go for consecutive complete clean
packets.  Abstract three-owner paths can overlap after a reservoir swap,
but the literal saturated suffix of the later packet then crosses the
earlier packet's disjoint rank-\(d\) bank.  Consequently complete packets
cannot share a protected Johnson edge, even with dynamic cores.  In the
exact un-enriched clean pattern, starts at distance two are also
impossible, so two packets cannot even share an owner occurrence.

## 1. Parameters and the two decisive local rows

Put

\[
 n=2m+1,\qquad L=d+2,\qquad a=m-d-2,
\qquad d\ge2.
\tag{1.1}
\]

Let \((A_t)\) be one set-valued source word.  A complete clean lag-two
packet beginning at \(s\) has a flag bottom

\[
 M_s=\bigcup_{t=s+2}^{s+L-2}A_t
     =\bigcup_{t=s+2}^{s+d}A_t,
\qquad |M_s|=a,
\tag{1.2}
\]

and a disjoint rank-\(d\) bank

\[
 C_s\subseteq A_{s+L-1}=A_{s+d+1},
\qquad |C_s|=d,
\qquad M_s\cap C_s=\varnothing.
\tag{1.3}
\]

In the standard clean packet, equality holds in (1.3).  Writing only
containment makes the argument robust under any redundant endpoint or
core enrichment.

The packet's length-\(d\) suffix immediately preceding its bank is the
upper endpoint \(U_s\) of its saturated promotion flag:

\[
 U_s=\bigcup_{t=s+1}^{s+d}A_t,
\qquad |U_s|=a+1,
\qquad M_s\subset U_s.
\tag{1.4}
\]

Only (1.2)--(1.4) will be needed.  In particular the proof below is
independent of the packet's fixed core, toggle order, owner labels, and
endpoint enrichments.

## 2. The abstract cross-core overlap equations are soluble

It is useful first to separate the owner-level equations from the literal
source obstruction.

For one clean packet, write

\[
 R=M\mathbin{\dot\cup}C,\qquad |R|=m-2,
\tag{2.1}
\]

so its three owners are

\[
 T_0=R\cup\{x,u\},\qquad
 T_1=R\cup\{u,y\},\qquad
 T_2=R\cup\{y,v\}.
\tag{2.2}
\]

Suppose a second abstract packet is intended to start one owner step
later.  Write its data as

\[
 T'_0=R'\cup\{x',u'\},\qquad
 T'_1=R'\cup\{u',y'\},\qquad
 T'_2=R'\cup\{y',v'\}.
\tag{2.3}
\]

The desired overlap is

\[
 T'_0=T_1,\qquad T'_1=T_2.
\tag{2.4}
\]

Taking the two directed differences and the common intersection gives

\[
 x'=u,\qquad y'=v,\qquad
 R'\cup\{u'\}=R\cup\{y\}.
\tag{2.5}
\]

Therefore every abstract solution is obtained by choosing

\[
 u'\in R\cup\{y\},
\qquad
 R'=(R\cup\{y\})\setminus\{u'\}.
\tag{2.6}
\]

There are two types:

\[
 \begin{array}{c|c}
 u'=y&R'=R,\\
 u'=r\in R&R'=R-r+y.
 \end{array}
\tag{2.7}
\]

Thus a cross-core or dynamic-reservoir swap does solve the two shared
owner equations.  There is no abstract Johnson-path obstruction.  The
failure occurs only when both packets are required to retain their
literal promotion flags.

## 3. Consecutive-start suffix-rank obstruction

### Theorem 3.1

No set-valued source word contains complete clean lag-two packets at both
starts \(s\) and \(s+1\) when \(d\ge2\).

This remains true if the packets use different fixed cores, adjacent
dynamic cores, different toggle streams, or source letters enriched by
coordinates redundant for their owner windows.

#### Proof

Apply (1.2)--(1.3) to the packet at \(s\).  Apply the saturated
length-\(d\) suffix row (1.4) to the packet at \(s+1\).  The latter suffix
occupies positions

\[
 (s+1)+1,\ldots,(s+1)+d
 =s+2,\ldots,s+d+1.
\tag{3.1}
\]

Its union contains both

\[
 \bigcup_{t=s+2}^{s+d}A_t=M_s
\tag{3.2}
\]

and

\[
 C_s\subseteq A_{s+d+1}.
\tag{3.3}
\]

Since \(M_s\cap C_s=\varnothing\), its rank is at least

\[
 |M_s\cup C_s|=a+d.
\tag{3.4}
\]

But (1.4) for the packet at \(s+1\) says that exactly the same union is
its flag endpoint \(U_{s+1}\), of rank \(a+1\).  Hence

\[
 a+d\le a+1,
\tag{3.5}
\]

forcing \(d\le1\), contrary to \(d\ge2\).  \(\square\)

### Corollary 3.2 (the obstruction precedes all core equations)

No choice of the abstract solution (2.6), and no equal-or-adjacent
rank-\(a\) core tracking, can lift two consecutive complete packets to one
literal word.  The rank contradiction uses neither \(R,R'\) nor the
cores.  Dynamic cores solve the owner projection but cannot move the
rank-\(d\) bank out of the later saturated suffix.

### Corollary 3.3 (same-start multiplicity is unavailable)

At a fixed start \(s\), the word uniquely determines \(M_s\) by (1.2) and
determines the unique rank-\((a+1)\) suffix \(U_s\) by (1.4).  Hence two
distinct prescribed promotion flags cannot be carried by the same clean
packet occurrence.

### Proposition 3.4 (exact clean packets cannot share an owner occurrence)

In the exact clean source pattern, the cells at positions \(s+L\) and
\(s+L+1\) are the singleton letters \(\{y_s\}\) and \(\{v_s\}\).
If a second exact packet starts at \(s+r\), its rank-\(d\) bank cell is at

\[
 s+r+L-1.
\tag{3.6}
\]

For \(r=1\), this is the first packet's \(y_s\)-singleton; for \(r=2\),
it is the \(v_s\)-singleton.  Equality with a rank-\(d\) bank forces
\(d=1\).  Hence, for \(d\ge2\), exact packet starts cannot differ by one
or two.

The owner-index block of a packet is \(\{s,s+1,s+2\}\).  Two distinct
such blocks overlap only when their starts differ by one or two.
Therefore exact clean packets cannot share any owner occurrence.

There is also an endpoint-enrichment-tolerant distance-two proof once
\(d\ge4\).  Inside the first saturated packet put

\[
 S_r=\bigcup_{t=s+r}^{s+d}A_t.
\tag{3.7}
\]

The one-rank-at-a-time suffix condition gives

\[
 |S_2|=a,\qquad |S_3|=a-1,\qquad |S_4|=a-2.
\tag{3.8}
\]

A packet at \(s+2\) would have bottom

\[
 M_{s+2}
 =S_4\cup A_{s+d+1}\cup A_{s+d+2}.
\tag{3.9}
\]

The last two cells contain the first packet's disjoint \(d\)-set \(C_s\)
and its new label \(y_s\notin M_s\cup C_s\).  Hence

\[
 |M_{s+2}|\ge(a-2)+d+1=a+d-1>a,
\tag{3.10}
\]

a contradiction.  Thus, in the eventual regime \(d\ge4\), even redundant
endpoint enrichment cannot permit owner-occurrence overlap.

For the finite cases \(d=2,3\), the exact clean singleton comparison above
is sufficient.  In any case, a hypothetical enriched distance-two
meeting would share only one owner, not a Johnson transition, and hence
would save no protected incidence edge.  The consecutive-start Theorem
3.1 is valid under all enrichments for every \(d\ge2\).

## 4. Exact protected-incidence consequence

Let

\[
 T_i=\bigcup_{t=i}^{i+L-1}A_t
\tag{4.1}
\]

be the rank-\(m\) owner chronology, and let

\[
 J_i=T_i\cup T_{i+1}
\tag{4.2}
\]

be its immediate upper chronology.  A complete packet at start \(s\)
uses the four-incidence-edge path

\[
 T_s\subset J_s\supset T_{s+1}
     \subset J_{s+1}\supset T_{s+2}.
\tag{4.3}
\]

Two distinct such paths share a physical Johnson transition precisely
when their starts differ by one.  Theorem 3.1 forbids this.  Starts at
distance two may share the endpoint owner \(T_{s+2}\), but their
transition-index sets

\[
 \{s,s+1\},\qquad\{s+2,s+3\}
\tag{4.4}
\]

are disjoint, so this concatenation saves no incidence edge.

In a one-copy owner and immediate-upper chronology, the same set-valued
transition also cannot be repeated at two separated occurrence indices.
Consequently, for \(h\) distinct complete clean packet tasks, their
protected union necessarily has

\[
 \boxed{2h\text{ distinct Johnson transitions and }4h
 \text{ distinct middle-levels incidence edges}.}
\tag{4.5}
\]

Thus a bundled train with one task per new Johnson transition, which
would have \(h+O(1)\) Johnson transitions and \(2h+O(1)\) incidence
edges, is impossible within the complete clean lag-two template.

For the triangular Ferrers bank,

\[
 h\le\binom{d+1}{2}.
\tag{4.6}
\]

The existing small-protected-subgraph theorem therefore still sees the
complete bank through the condition

\[
 4h\le m-1,
\tag{4.7}
\]

not through \(2h+O(1)\le m-1\).  At the worst permitted task count,

\[
 4h\le 2d(d+1)
      =\left(\frac{\pi}{2}+o(1)\right)m,
\tag{4.8}
\]

so the desired scalar improvement cannot come from cross-core packet
overlap.

## 5. Audit of the dynamic-core normal form

The two relevant claims in
MATH_THEOREM_PBBS_FIXED_CORE_COLLAR_UNBORDERED_AND_DYNAMIC_CORE_FACTOR_NORMAL_FORM_20260807.md
pass their local checks.

First, for \(d\ge3\), the same-core fragment word

\[
 C_0,\ \varnothing,\ H^{d-1},\
 C_0,\ \varnothing,\ \varnothing
\tag{5.1}
\]

is unbordered in the stated literal sense.  Comparing full source-letter
ranks forces a nonzero overlap to begin at the second \(C_0\)-position;
the third shared position then compares a nonempty \(H\)-fragment with an
empty fragment.  When the two collars use the same \(G\), equality at the
first shared position also identifies their core part \(C_0\), because
all designated toggles lie outside \(G\).  The \(d=2\) periodic fragment
exception is correctly separated.

There is also a useful strengthening.  When \(m>3d\), the ranks of the
full exceptional source letters are

\[
 d,\ 1,\ (m-2d)^{d-1},\ d,\ 1,\ 1.
\tag{5.2}
\]

This rank word is itself unbordered.  Its initial rank \(d\) can align
with a later position only at the second rank-\(d\) cell, a shift of
\(d+1=L-1\).  The resulting length-three comparison is

\[
 (d,1,1)\quad\text{against}\quad(d,1,m-2d),
\tag{5.3}
\]

which fails because \(m-2d>d\).  Consequently, for sufficiently large
parameters, the fixed-core collar theorem extends to collars with
**arbitrary different cores**: their exact exceptional supports cannot
overlap at all.  The shared-core decomposition is not needed for this
stronger rank argument.

Second, the dynamic-core recurrence is exact.  If

\[
 T_{i+1}=T_i-x_i+y_i,\qquad G_i\subset T_i,\qquad |G_i|=a,
\tag{5.4}
\]

then:

* if \(x_i\notin G_i\), taking \(G_{i+1}=G_i\) gives
  \(Q_{i+1}=Q_i-x_i+y_i\);
* if \(x_i\in G_i\), any
  \(w_i\in(T_i\cap T_{i+1})\setminus G_i\) gives

  \[
  G_{i+1}=G_i-x_i+w_i,\qquad
  Q_{i+1}=Q_i-w_i+y_i.
  \tag{5.5}
  \]

The choice set in the second case has size

\[
 |(T_i\cap T_{i+1})\setminus G_i|
 =(m-1)-(a-1)=m-a=L>0.
\tag{5.6}
\]

Hence every abstract owner path has the claimed equal-or-adjacent core
lift.  Theorem 3.1 shows exactly why that result does not imply a bundled
promotion train: the recurrence tracks owner decompositions, whereas the
contradiction lies in two overlapping shorter suffix rows.

## 6. Scope and surviving routes

The no-go is specific and sharp:

\[
 \boxed{\text{complete clean lag-two packets cannot share a Johnson
 transition when }d\ge2.}
\tag{6.1}
\]

It does not rule out nearby packets whose paths meet only at an owner, but
those retain the full \(4h\) incidence cost.  It also does not rule out a
new local promotion template with a different placement of the rank-\(d\)
bank.

Accordingly, reducing the current protected-factor burden requires at
least one genuine change of route:

1. retain the two-incidence-edge punctured projection and separately
   discharge its authoritative forced-coatom ticket;
2. prove the co-selected protected \(b\)-factor inequalities directly
   for the full \(4h\)-edge bank; or
3. invent a non-clean bundled template in which the previous task's
   rank-\(d\) bank does not lie inside the next task's rank-\((a+1)\)
   saturated suffix.

Changing only the fixed or dynamic core cannot overcome (3.4).
