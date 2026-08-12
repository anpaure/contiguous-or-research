# Lane N: exact escape from the full MSW orbit and a depth-one balanced cycle

## Status and exact boundary

This report proves two positive theorems.

1. For every fixed \(\varepsilon>0\) and all sufficiently large \(m\),
   there is a deterministic sequence of legal ownership-component switches
   from the canonical MSW exact wreath factor to an exact wreath factor
   \(G_m\) satisfying
   \[
   d_{\rm row}\bigl(G_m,S_{2m+1}F_m^{\rm MSW}\bigr)
   >\left(\frac{3}{16}-\varepsilon\right)\operatorname{Cat}_m.
   \]
   Every state of the sequence is one integral exact wreath factor.  Every
   individual switch replaces only \(O_\varepsilon(1)\) wreath packets, and
   the total number of replaced packets is \(O(\operatorname{Cat}_m)=o(W)\).
   In particular, taking \(\varepsilon<1/16\) exits the entire audited
   \((1/8-o(1))\operatorname{Cat}_m\) MSW-orbit basin, not just the basin of
   one labelled representative.

2. For \(m\ge 6\), there is a Hamilton cycle in the Johnson graph
   \(J(2m+1,m)\) whose rank-\((m-1)\) intersection colours have exactly the
   scalar floor profile: every colour occurs once and exactly
   \(2W/(m+2)\) colours occur a second time.  Cutting one duplicate edge of
   each high colour gives a spanning rainbow Johnson linear forest with
   exactly \(2W/(m+2)\) components.  The audited one-step MTF lift therefore
   gives a literal OR word of length
   \[
   W+\frac{6W}{m+2}=W+o(W)
   \]
   covering ranks \(m-1\) and \(m\).

The first theorem is the requested deterministic route out of the full MSW
basin.  It does **not** prove that its endpoint has shallow overload
\(o(W)\), and it does not carry an adaptive adjacent-deletion orientation.
The second theorem solves the scalar depth-one Hall/cyclomatic relaxation,
but its Hamilton cycle need not packetize into genuine length-\((2m+1)\)
wreaths and its high family need not have the point margins forced on an
exact factor.  Thus neither theorem alone proves the constant-one conjecture.

All factors and switches below are integral.  No fractional mixture is
promoted to a factor.

## 1. Notation

Put
\[
n=2m+1,
\qquad
W=\binom{n}{m},
\qquad
B=\frac Wn=\operatorname{Cat}_m.
\]

A wreath packet is an unoriented cyclic packet of the \(n\) consecutive
\(m\)-intervals of a cyclic coordinate order.  An exact wreath factor is a
set of \(B\) packets whose owner sets partition \(\binom{[n]}m\).  For two
exact factors, define
\[
d_{\rm row}(F,G)
=B-|F\cap G|
=\frac12|F\mathbin\triangle G|.
\tag{1.1}
\]

Let \(F_m=F_m^{\rm MSW}\), and fix the coordinate transposition
\[
\tau=(2\ 3).
\]
For \(m\ge2\), packet rigidity and the existence of a \(\tau\)-fixed owner
inside every wreath imply
\[
F_m\cap\tau F_m=\varnothing.
\tag{1.2}
\]
Indeed, a length-\(m\) cyclic interval fixed as a set by \(\tau\) exists
because the sum, over all \(n\) cyclic intervals, of the numbers of the two
transposed coordinates present is \(2m<n\).  If both a packet and its
\(\tau\)-image occurred in one exact factor, they would share this owner.
They would then have to be the same packet, which is impossible because a
single transposition is not in the dihedral stabilizer of an odd cyclic
order when \(n\ge5\).

## 2. The exact MSW component hierarchy

Overlay the owner partitions of \(F_m\) and \(\tau F_m\).  Its connected
components have two packet sides \(L_i\subset F_m\) and
\(R_i=\tau L_i\subset\tau F_m\), which partition the same owner block
\(\Omega_i\).  If \(|L_i|=|R_i|=s_i\), then
\[
|\Omega_i|=ns_i.
\tag{2.1}
\]
Choosing either whole side independently in every component preserves every
middle owner exactly once, hence gives another exact wreath factor.

We use the proved MSW hierarchy:
\[
s_j=\operatorname{Cat}_j+\operatorname{Cat}_{j+1},
\qquad
k_{m,j}=\operatorname{Cat}_{m-j-2},
\qquad 0\le j\le m-2,
\tag{2.2}
\]
where there are exactly \(k_{m,j}\) components of side size \(s_j\).  Its
mass identity is
\[
\sum_{j=0}^{m-2}k_{m,j}s_j=B.
\tag{2.3}
\]

Fix an integer \(J\ge0\).  Let \(\mathcal I_{m,J}\) be all components of
types \(0\le j\le J\), and put
\[
S_{m,J}
=\sum_{j=0}^{J}\operatorname{Cat}_{m-j-2}s_j,
\qquad
Q_{m,J}
=\sum_{j=0}^{J}\operatorname{Cat}_{m-j-2}s_j^2.
\tag{2.4}
\]
Here \(S_{m,J}\) is the number of MSW packets on the chosen sides of these
components, while \(Q_{m,J}\) is their squared side-size ledger.  Since
\(s_j\) is increasing,
\[
Q_{m,J}\le s_JS_{m,J}\le s_JB.
\tag{2.5}
\]

### Lemma 2.1 (the bounded-component row mass)

For fixed \(J\),
\[
\frac{S_{m,J}}B\longrightarrow
p_J:=\sum_{j=0}^{J}\frac{s_j}{4^{j+2}}.
\tag{2.6}
\]
Moreover
\[
p_J\uparrow\frac38.
\tag{2.7}
\]

#### Proof

For fixed \(r\),
\[
\frac{\operatorname{Cat}_{m-r}}{\operatorname{Cat}_m}
\longrightarrow 4^{-r}.
\]
This gives (2.6).  If
\(C(z)=\sum_{j\ge0}\operatorname{Cat}_jz^j\), then
\(C(1/4)=2\).  Consequently
\[
\begin{aligned}
\sum_{j\ge0}\frac{\operatorname{Cat}_j}{4^{j+2}}
&=\frac18,\\
\sum_{j\ge0}\frac{\operatorname{Cat}_{j+1}}{4^{j+2}}
&=\frac14,
\end{aligned}
\]
which proves (2.7). \(\square\)

The order of limits is important: below \(\varepsilon\) is fixed first,
then a fixed \(J=J(\varepsilon)\) is chosen, and only then does
\(m\to\infty\).

## 3. The decisive external-factor capacity inequality

Let \(H\) be any exact wreath factor, not necessarily in the MSW orbit.
For a component \(i\), define
\[
a_i=|H\cap L_i|,
\qquad
b_i=|H\cap R_i|.
\tag{3.1}
\]

### Lemma 3.1 (one component cannot occupy both sides densely)

For every component,
\[
\boxed{a_i+b_i\le s_i.}
\tag{3.2}
\]

#### Proof

Every packet in \(L_i\cup R_i\) has all of its \(n\) middle owners inside
\(\Omega_i\).  The packets of the exact factor \(H\) have pairwise disjoint
owner sets.  Since \(|\Omega_i|=ns_i\), at most \(s_i\) packets of \(H\)
can belong to \(L_i\cup R_i\).  Equation (3.2) follows. \(\square\)

This owner-block argument is the point that makes a union bound over the
entire MSW orbit possible.  It uses exact middle ownership and would be false
for arbitrary signed packet vectors.

Independently choose \(L_i\) or \(R_i\), with probability \(1/2\), for every
\(i\in\mathcal I_{m,J}\), and retain \(L_i\) on every other component.  Call
the resulting random exact factor \(G\).  For a fixed exact factor \(H\), put
\[
D_i=
\begin{cases}
s_i-a_i,&\text{if }L_i\text{ is chosen},\\
s_i-b_i,&\text{if }R_i\text{ is chosen}.
\end{cases}
\tag{3.3}
\]
By (3.2),
\[
\mathbb E D_i
=s_i-\frac{a_i+b_i}{2}
\ge\frac{s_i}{2},
\tag{3.4}
\]
and the range length of \(D_i\) is
\[
|a_i-b_i|\le s_i.
\tag{3.5}
\]
The rows chosen on components outside \(\mathcal I_{m,J}\) can only add to
the row distance from \(H\), so exactly
\[
d_{\rm row}(G,H)
\ge\sum_{i\in\mathcal I_{m,J}}D_i.
\tag{3.6}
\]

## 4. Full-orbit escape

### Theorem 4.1 (exact escape from every relabelled MSW basin)

For every \(\varepsilon>0\), for all sufficiently large \(m\), there is an
exact wreath factor \(G_m\) in the \(F_m/\tau F_m\) component-switch cube
such that
\[
\boxed{
d_{\rm row}\bigl(G_m,S_nF_m\bigr)
>\left(\frac{3}{16}-\varepsilon\right)B.}
\tag{4.1}
\]
The switches needed to reach \(G_m\) from \(F_m\) use only component types
\(j\le J(\varepsilon)\), and hence each switch replaces at most
\[
s_{J(\varepsilon)}
=\operatorname{Cat}_{J(\varepsilon)}
 +\operatorname{Cat}_{J(\varepsilon)+1}
\tag{4.2}
\]
packets on either side.

#### Proof

Fix \(\varepsilon>0\).  Choose a fixed \(J\) so that
\[
p_J>\frac38-\frac\varepsilon2.
\tag{4.3}
\]
By Lemma 2.1, for all sufficiently large \(m\),
\[
\frac{S_{m,J}}B>\frac38-\varepsilon.
\tag{4.4}
\]

Fix one conjugate \(H=\sigma F_m\).  Set
\[
T=\left(\frac{3}{16}-\varepsilon\right)B.
\]
Equations (3.4) and (4.4) give
\[
\sum_i\mathbb ED_i-T
\ge\frac{S_{m,J}}2-T
>\frac\varepsilon2 B.
\tag{4.5}
\]
Hoeffding's inequality, (3.5), and (2.5) therefore give
\[
\begin{aligned}
\Pr\bigl(d_{\rm row}(G,H)\le T\bigr)
&\le
\Pr\left(\sum_iD_i\le T\right)\\
&\le
\exp\left(
-\frac{2(\varepsilon B/2)^2}{Q_{m,J}}
\right)\\
&\le
\exp\left(-\frac{\varepsilon^2B}{2s_J}\right).
\end{aligned}
\tag{4.6}
\]

There are at most \(n!\) labelled conjugates.  Since
\[
\log(n!)=O(m\log m)=o(B),
\tag{4.7}
\]
the union bound from (4.6) is less than one for all sufficiently large
\(m\).  Hence some component choice satisfies (4.1) simultaneously for
every \(\sigma\in S_n\).  Every such choice is an exact factor because each
whole ownership component is replaced by its other exact side. \(\square\)

For completeness, (4.7) needs no delicate asymptotic estimate.  The largest
binomial coefficient in row \(2m\) is at least \(2^{2m}/(2m+1)\), so
\[
B=\frac1{m+1}\binom{2m}{m}
\ge\frac{4^m}{(m+1)(2m+1)},
\]
which dominates \(m\log m\).

### Corollary 4.2 (deterministic bounded-switch route)

The endpoint in Theorem 4.1 can be selected deterministically, and there is
a deterministic exact-factor history
\[
F_m=F^{(0)},F^{(1)},\ldots,F^{(t)}=G_m
\tag{4.8}
\]
such that each step switches one component of side size at most \(s_J\).
Moreover
\[
t\le\sum_{j=0}^{J}\operatorname{Cat}_{m-j-2}=O_\varepsilon(B),
\tag{4.9}
\]
and the total number of old packets replaced, counted once, is at most
\[
S_{m,J}le B=\frac Wn=o(W).
\tag{4.10}
\]

#### Proof

Order the components in \(\mathcal I_{m,J}\) canonically.  Let \(Z\) be the
number of conjugates \(\sigma F_m\) for which the final random completion
violates (4.1).  The proof of Theorem 4.1 gives \(\mathbb EZ<1\).  At each
component, choose the side for which the conditional expectation of \(Z\)
is no larger; the average of the two conditional expectations is the
current one.  After all choices, \(Z\) is an integer smaller than one, hence
zero.  Breaking ties in favour of \(L_i\) makes the rule deterministic.

Starting from \(F_m\), switch precisely the components ultimately assigned
their \(R_i\) side, in the same canonical order.  Disjoint ownership blocks
make every intermediate state an exact factor.  The bounds (4.9)--(4.10)
are immediate from (2.2) and (2.4). \(\square\)

This is an existence-level deterministic method; no claim of polynomial-time
evaluation of the conditional expectations is made.

### Exact implication for the old basin obstruction

The audited all-conjugate singular-boundary theorem says that an exact factor
supporting an \(o(W)\)-cost AO history must have distance at least
\((1/8-o(1))B\) from \(S_nF_m\).  If \(\varepsilon<1/16\), then
\[
\frac{3}{16}-\varepsilon>\frac18.
\tag{4.11}
\]
Thus Theorem 4.1 constructs exact factors strictly beyond the whole forbidden
orbit basin.  The basin condition is therefore not an emptiness obstruction
in exact-factor space.

The row-volume statement (4.10) must not be misread as an AO-cost bound.
Switching one packet changes \(n\) middle owners, so the owner volume along
this route can be \(\Theta(W)\), and no adjacent-deletion orientation is
transported.

## 5. A scalar floor-balanced depth-one Hamilton cycle

This section is independent of the MSW component argument.

Let
\[
\mathcal L=\binom{[n]}{m-1},
\qquad
\mathcal M=\binom{[n]}m,
\qquad
N=|\mathcal L|.
\]
Then
\[
N=\frac{m}{m+2}W,
\qquad
\rho:=W-N=\frac{2W}{m+2}.
\tag{5.1}
\]

We use the proved saturating-cycle theorem for consecutive Boolean levels:
the inclusion graph between \(\mathcal L\) and \(\mathcal M\) has an
alternating cycle containing every vertex of \(\mathcal L\) and exactly
\(N\) vertices of \(\mathcal M\).  Contracting each lower vertex gives a
Johnson cycle on those \(N\) middle vertices, with every lower intersection
colour used exactly once.

Let \(\mathcal U\subset\mathcal M\) be the \(\rho\) omitted middle vertices.

### Lemma 5.1 (distinct facet representatives for the omitted owners)

If \(m\ge6\), there is an injection
\[
f:\mathcal U\longrightarrow\mathcal L,
\qquad f(U)\subset U.
\tag{5.2}
\]

#### Proof

It is enough to verify Hall.  Let \(\mathcal A\subseteq\mathcal U\).  The
exact inequality
\[
\rho\le\binom{2m-1}{m}
\tag{5.3}
\]
is equivalent to
\[
4(2m+1)\le(m+1)(m+2),
\]
or \(m^2-5m-2\ge0\), and hence holds for \(m\ge6\).

Write \(|\mathcal A|=\binom{x}{m}\) for real \(x\ge m\).  By the
Lovasz--Kruskal--Katona shadow theorem and (5.3), \(x\le2m-1\), so
\[
|\partial\mathcal A|
\ge\binom{x}{m-1}
=\frac{m}{x-m+1}|\mathcal A|
\ge|\mathcal A|.
\tag{5.4}
\]
Hall's theorem gives (5.2). \(\square\)

### Theorem 5.2 (one Hamilton cycle attains the scalar \(q=1\) floor)

For \(m\ge6\), there is a Hamilton cycle \(\Gamma\) on all \(W\) vertices
of \(J(n,m)\) and a family \(\mathcal H\subset\mathcal L\),
\(|\mathcal H|=\rho\), such that its edge-intersection multiplicities are
\[
\mu_\Gamma(S)=
\begin{cases}
2,&S\in\mathcal H,\\
1,&S\notin\mathcal H.
\end{cases}
\tag{5.5}
\]

#### Proof

Take the contracted saturating cycle.  For every \(U\in\mathcal U\), let
\(S=f(U)\).  The unique cycle edge coloured \(S\) has endpoints
\(X=S\cup\{a\}\) and \(Y=S\cup\{b\}\).  Replace
\[
X-Y
\quad\text{by}\quad
X-U-Y.
\tag{5.6}
\]
Both new edges have intersection colour \(S\).  The representatives
\(f(U)\) are distinct, so these subdivisions occur on distinct cycle edges.
After all \(\rho\) subdivisions, every omitted middle vertex has been
inserted exactly once and the result is one Hamilton cycle.  A matched colour
has had one occurrence replaced by two, while every other colour is
unchanged.  Taking \(\mathcal H=f(\mathcal U)\) proves (5.5). \(\square\)

Because \(c_1=1\) and the residual quota is \(\rho=W-N\), (5.5) is exactly
zero scalar depth-one overload.

### Corollary 5.3 (literal coefficient one for ranks \(m-1,m\))

For \(m\ge6\), there is a literal contiguous-OR word of length at most
\[
\boxed{W+3\rho=W+\frac{6W}{m+2}}
\tag{5.7}
\]
covering every set of ranks \(m-1\) and \(m\).

#### Proof

For each inserted vertex \(U\), the two incident edges created in (5.6)
have the same colour \(f(U)\).  Delete one of these two edges.  The deleted
edges are distinct.  Removing \(\rho\) edges from the Hamilton cycle leaves
a spanning linear forest with exactly \(\rho\) components, isolated vertices
allowed.  Exactly one edge of every lower colour remains.

At every internal middle vertex the two surviving intersection facets are
distinct.  Equivalently, along every oriented path, a newly arriving
coordinate is not the coordinate departed at the next step.  Thus there is
no internal positive coordinate run of length one.  The endpoint data for
the one-step lift always exist explicitly.  For a path
\(T_0,\ldots,T_{K-1}\) with \(K\ge2\), choose an initial upper singleton
\(u\notin T_0\) and a terminal dummy departure
\(v\in T_{K-2}\cap T_{K-1}\).  For an isolated vertex \(K=1\), choose
\(u\notin T_0\) and any \(v\in T_0\).

Apply the audited \(H=1\) canonical MTF lift separately to the \(\rho\)
paths.  A path with \(K\) middle vertices costs exactly \(K+3\) nonempty
word entries and exposes every middle vertex and every lower colour of its
edges.  Summing \(K=W\) over the paths gives (5.7), and all \(N\) lower
colours occur. \(\square\)

## 6. Point margins and packetization: the remaining exact gate

The high family \(\mathcal H\) in Theorem 5.2 is obtained only as a system
of distinct facet representatives.  An exact wreath factor has the fixed
depth-one point margins
\[
\sum_{S\ni x}\mu_1(S)=(m-1)B
\qquad(x\in[n]).
\tag{6.1}
\]
Since the all-one base on \(\mathcal L\) contributes
\(\binom{2m}{m-2}\) at each point, a floor high family compatible with an
exact factor would have to satisfy
\[
\deg_{\mathcal H}(x)
=\frac{2(m-1)}{m+2}B
\qquad(x\in[n]).
\tag{6.2}
\]
Lemma 5.1 does not impose (6.2).

There is a second, independent packetization condition.  A Johnson cycle of
length \(n\) is a genuine wreath precisely when its entering labels are a
bijection of \([n]\) and every coordinate has residence \(m\).  The Hamilton
cycle in Theorem 5.2 is not shown to decompose into \(B\) cycles with these
properties.  Therefore it is not promoted to an exact wreath factor.

The precise surviving positive exact-factor gate is:

> Select the bounded-component MSW switches of Theorem 4.1 so that the
> resulting distant exact factor also has fixed-window overload \(o(W)\), or
> packetize a point-regular refinement of Theorem 5.2 into genuine wreath
> cycles with only \(o(W)\) shadow loss.

Neither assertion is proved here.  In particular, row distance beyond the
MSW basin, scalar depth-one balance, point-regularity, exact wreath
packetization, and adaptive AO history are five distinct conditions.

## 7. Independent audit record

The decisive full-orbit step was independently rederived.  The audit checked:

1. \(a_i+b_i\le s_i\) from exact owner-block capacity;
2. the range constant in Hoeffding's inequality;
3. \(S_{m,J}/B\to p_J\uparrow3/8\);
4. the exponent \(\varepsilon^2B/(2s_J)\);
5. the \(n!\) union bound and the fixed-\(J\) order of limits;
6. conditional-expectation derandomization;
7. exact-factor integrality at every component switch; and
8. the distinction between \(O(B)\) packet turnover and potentially
   \(\Theta(W)\) owner/AO transport.

The depth-one cycle proof was separately audited through the exact inequality
\(m^2-5m-2\ge0\), the Lovasz--Kruskal--Katona ratio, the distinct-edge
subdivision, the scalar floor count, and the point-margin caveat.
