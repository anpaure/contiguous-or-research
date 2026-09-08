# Exact degrees for the annulus cyclic-order hypergraph and the coloured partial-factor gate

Date: 2026-07-26

Method: pure mathematics only. No computation, web input, solver, or
probabilistic black box is used.

## 0. Outcome

Put

\[
 n=2m,\qquad R=m-q_0,\qquad
 W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},
\tag{0.1}
\]

where

\[
 q_0=\lceil a\sqrt m\rceil,\qquad
 H=\lfloor b\sqrt m\rfloor,
 \qquad 0<a<b<\infty.
\tag{0.2}
\]

The corrected packet number is

\[
 K_0=\left\lfloor\frac{N_{q_0}}{2m}\right\rfloor.
\tag{0.3}
\]

A packet is a directed cyclic order on \([n]\), modulo rotation. At rank
\(s\), its trace is the set of its \(n\) cyclic intervals of length \(s\).
The rank-\(R\) packet hypergraph is exactly regular. Its vertex degree is

\[
 d_R=R!(n-R)!,
\tag{0.4}
\]

and the codegree of two distinct \(R\)-sets with intersection size \(t\)
is

\[
 \lambda_R(t)=
 \begin{cases}
 R!^2(n-2R+1)!,&t=0,\\[2mm]
 2(R-t)!^2t!(n-2R+t)!,&1\le t\le R-1.
 \end{cases}
\tag{0.5}
\]

For the Gaussian value \(R=m-q_0\), the maximum is attained at
\(t=R-1\) for all sufficiently large \(m\), and hence

\[
 \boxed{
 \frac{\Delta_2}{d_R}=\frac{2}{R(n-R)}
       =\frac{2+o(1)}{m^2}.}
\tag{0.6}
\]

The maximum alone conceals further sparsity. If two packets through the
same rank-\(R\) target are chosen independently and uniformly, their
expected number of additional common rank-\(R\) targets is

\[
 \boxed{
 \Gamma_R
 =\frac{4}{R(n-R)}+O(m^{-4})
 =\frac{4+o(1)}{m^2}.}
\tag{0.7}
\]

Thus only the two neighboring intervals create the largest codegree; the
rest of an edge contributes two orders less.

Middle-owner collisions can be incorporated rather than repaired. Quotient
the middle layer by complementation. A packet uses \(m\) antipodal middle
pairs. On that shore the degree is \(d_m=m!^2\), and the maximum normalized
codegree between distinct antipodal pairs is again exactly \(2/m^2\).
The cross-codegree between a rank-\(R\) target and an antipodal middle pair
is superpolynomially smaller than either degree.

The uniform weight

\[
 x_\pi=\frac1{d_R}
\tag{0.8}
\]

is consequently an exact fractional matching on the rank-\(R\) shore,
uses total packet mass \(N_{q_0}/n\), and puts load

\[
 \alpha_m=\frac{d_m}{d_R}
 =\frac{N_{q_0}}W=e^{-a^2+o(1)}<1
\tag{0.9}
\]

on every antipodal middle pair. This gives constant slack against middle
collisions.

The integral problem is nevertheless not an ordinary near-matching. At
rank \(R-1\), every packet colors each edge of its rank-\(R\) trace cycle
by the intersection of its endpoints. At rank \(R-d\), it colors every
directed \(d\)-path by the intersection of its \(d+1\) vertices. These
path colors are already fixed when the rank-\(R\) packet is selected. The
remaining theorem is therefore one precise coloured partial-factor lemma,
stated in Section 8. Exact degrees and codegrees remove a local-capacity
obstruction, but they do not by themselves prove the needed correlated
integral rounding.

## 1. The packet hypergraphs

Let \(\Omega_n\) be the set of directed cyclic orders on \([n]\), modulo
cyclic rotation. Thus

\[
 |\Omega_n|=(n-1)!.
\tag{1.1}
\]

For \(\pi=(\pi_0,\ldots,\pi_{n-1})\in\Omega_n\), indices being cyclic,
write

\[
 I_\pi(j,s)=\{\pi_j,\pi_{j+1},\ldots,\pi_{j+s-1}\}
\tag{1.2}
\]

and

\[
 E_s(\pi)=\{I_\pi(j,s):j\in\mathbb Z_n\}.
\tag{1.3}
\]

For \(1\le s<n\), the members of \(E_s(\pi)\) are distinct. Define the
\(n\)-uniform hypergraph

\[
 \mathcal H_s
 =\left(\binom{[n]}s,\{E_s(\pi):\pi\in\Omega_n\}\right).
\tag{1.4}
\]

We retain the directed catalogue. Reversal gives two catalogue elements
with the same unoriented interval set. If one instead takes the simple
dihedral quotient, all degrees and codegrees below are divided by two and
all normalized ratios are unchanged.

At the annulus entrance, \(s=R=m-q_0<n/2\). A matching of size \(K_0\)
in \(\mathcal H_R\) covers \(nK_0=N_{q_0}-\rho\) distinct entrance
targets, where

\[
 0\le \rho=N_{q_0}-nK_0<n.
\tag{1.5}
\]

The rounding leave is therefore negligible.

## 2. Exact degree and pair codegree

### Lemma 2.1 (degree)

For every \(s\)-set \(A\),

\[
 d_s:=|\{\pi:A\in E_s(\pi)\}|=s!(n-s)!.
\tag{2.1}
\]

#### Proof

Regard \(A\) as one cyclic block. Its elements have \(s!\) internal
orders. Together with the \(n-s\) outside labels, there are \(n-s+1\)
objects, with \((n-s)!\) cyclic orders. \(\square\)

### Lemma 2.2 (two intervals of equal length)

Let \(s<n/2\), and let \(A,B\) be distinct \(s\)-sets with
\(|A\cap B|=t\). Then their codegree in \(\mathcal H_s\) is

\[
 \lambda_s(t)=
 \begin{cases}
 s!^2(n-2s+1)!,&t=0,\\[2mm]
 2(s-t)!^2t!(n-2s+t)!,&1\le t\le s-1.
 \end{cases}
\tag{2.2}
\]

#### Proof

If \(t=0\), the two sets are disjoint blocks. There are \(n-2s\)
outside labels, hence \(n-2s+2\) cyclic objects. This gives

\[
 s!^2(n-2s+1)!.
\]

Suppose \(t>0\). Since \(2s<n\), the union of the two cyclic intervals
does not fill the circle. Their intersection is one interval, and their
union is one interval. In one of the two possible orientations, the union
has the consecutive form

\[
 (A\setminus B),\quad(A\cap B),\quad(B\setminus A).
\]

The three internal orders contribute
\((s-t)!t!(s-t)!\). Treating the union as one block leaves
\(n-2s+t\) outside labels and hence \((n-2s+t)!\) external cyclic
orders. Multiplication by the two orientations proves (2.2). \(\square\)

### Proposition 2.3 (the Gaussian maximum)

For \(R=m-q_0\), with \(q_0=\Theta(\sqrt m)\),

\[
 \Delta_2=\lambda_R(R-1)
 =2(R-1)!(n-R-1)!
\tag{2.3}
\]

for all sufficiently large \(m\). Consequently (0.6) holds.

#### Proof

For \(1\le t\le R-2\),

\[
 \frac{\lambda_R(t+1)}{\lambda_R(t)}
 =\frac{(t+1)(n-2R+t+1)}{(R-t)^2}.
\tag{2.4}
\]

The right side increases with \(t\), so the sequence is first decreasing
and then increasing. Its maximum is at \(t=1\) or \(t=R-1\). Moreover

\[
 \frac{\lambda_R(1)}{\lambda_R(R-1)}
 =\frac{(R-1)!(2q_0+1)!}{(n-R-1)!}
 =\frac{2q_0+1}{\binom{n-R-1}{R-1}}
 =\exp\!\left[-\Theta\!\left(q_0\log\frac m{q_0}\right)\right].
\tag{2.5}
\]

The disjoint value obeys the same superpolynomial comparison:

\[
 \frac{\lambda_R(0)}{\lambda_R(R-1)}
 =\frac{R(2q_0)(2q_0+1)}
        {2\binom{n-R-1}{R}}
 =\exp\!\left[-\Theta\!\left(q_0\log\frac m{q_0}\right)\right].
\tag{2.6}
\]

This proves (2.3), and division by \(d_R\) gives (0.6). \(\square\)

The identity

\[
 \sum_{t=0}^{R-1}
 \binom Rt\binom{n-R}{R-t}\lambda_R(t)
 =(n-1)d_R
\tag{2.7}
\]

is a useful check: both sides count a packet through a fixed \(R\)-set
and a second interval in that packet.

## 3. The stronger edge-conditioned overlap moment

Fix \(A\in\binom{[n]}R\). Choose independently and uniformly two packets
\(P,P'\) through \(A\). Define

\[
 \Gamma_R
 =\mathbb E\bigl[|(E_R(P)\cap E_R(P'))\setminus\{A\}|\bigr].
\tag{3.1}
\]

### Proposition 3.1 (exact collision sum)

One has

\[
 \Gamma_R
 =2\sum_{t=1}^{R-1}\frac{\lambda_R(t)}{d_R}
 +(n-2R+1)\frac{\lambda_R(0)}{d_R}.
\tag{3.2}
\]

For \(q_0=\Theta(\sqrt m)\), this is (0.7).

#### Proof

In any fixed packet through \(A\), the two intervals at cyclic displacement
\(k\), \(1\le k\le R-1\), have intersection size \(R-k\). Hence there
are two other packet vertices of every intersection size
\(1,\ldots,R-1\). The remaining \(n-2R+1\) vertices are disjoint from
\(A\). Conditional on containing \(A\), a second packet contains a given
\(B\) with probability \(\lambda_R(|A\cap B|)/d_R\). This proves
(3.2).

The term \(t=R-1\) equals

\[
 2\frac{\lambda_R(R-1)}{d_R}
 =\frac4{R(n-R)}.
\]

The next term is

\[
 2\frac{\lambda_R(R-2)}{d_R}
 =\frac{16}{R(R-1)(n-R)(n-R-1)}=O(m^{-4}).
\]

Repeated use of (2.4), together with the superpolynomially small opposite
endpoint and disjoint terms from (2.5)--(2.6), shows that all remaining
terms sum to
\(O(m^{-6})+exp[-\Omega(q_0\log(m/q_0))]\). This proves (0.7).
\(\square\)

The distinction between (0.6) and (0.7) matters. If the edge size is
\(n\), then

\[
 n\frac{\Delta_2}{d_R}=O(m^{-1}),
 \qquad
 n^2\frac{\Delta_2}{d_R}=\Theta(1),
\tag{3.3}
\]

so a growing-uniformity theorem cannot be invoked merely by quoting a
fixed-rank nibble. But the actual overlap moment is \(O(m^{-2})\), since
only two positions attain \(\Delta_2\). A positive integral proof should
use (3.2), not replace the entire packet by its worst pair.

## 4. Exact mixed-size codegrees

The all-depth problem needs incidences between different ranks.

### Lemma 4.1 (two intervals of unequal lengths)

Let \(a\ge b\), \(a+b<n\), and fix
\(A\in\binom{[n]}a\), \(B\in\binom{[n]}b\) with
\(|A\cap B|=t\). The number of directed cyclic orders in which both sets
are intervals is

\[
 \Lambda_{a,b}(t)=
 \begin{cases}
 a!b!(n-a-b+1)!,&t=0,\\[2mm]
 2(a-t)!t!(b-t)!(n-a-b+t)!,&1\le t\le b-1,\\[2mm]
 b!(a-b+1)!(n-a)!,&t=b.
 \end{cases}
\tag{4.1}
\]

#### Proof

The disjoint and partially overlapping cases are the same block counts as
in Lemma 2.2. If \(t=b\), then \(B\subseteq A\). Internally, the block
\(A\) has

\[
 b!(a-b+1)!
\]

linear orders in which \(B\) is consecutive. Externally, the \(A\)-block
and the \(n-a\) remaining labels have \((n-a)!\) cyclic orders. \(\square\)

In particular, every pair of ranks in the controlled annulus has an exact
intersection-profile codegree, rather than merely an averaged incidence.
This is the coefficient table needed by any multi-depth switching or
absorption argument.

### Corollary 4.2 (the first nested cross-rank spine)

Let \(A\in\binom{[n]}R\), let
\(B\in\binom{[n]}{R-d}\), and suppose \(B\subset A\). Then

\[
 \frac{|\{\pi:A\in E_R(\pi),\ B\in E_{R-d}(\pi)\}|}{d_R}
 =\frac{d+1}{\binom Rd}.
\tag{4.2}
\]

In particular, for a nested entrance/first-shadow pair,

\[
 \boxed{
 \frac{|\{\pi:A\in E_R(\pi),\ B\in E_{R-1}(\pi)\}|}{d_R}
 =\frac2R=\Theta(m^{-1}).}
\tag{4.3}
\]

#### Proof

Use the containment line of (4.1) with \(a=R,b=R-d\), and divide by
\(R!(n-R)!\):

\[
 \frac{(R-d)!(d+1)!(n-R)!}{R!(n-R)!}
 =\frac{d+1}{\binom Rd}.
\]

\(\square\)

Thus the entrance hypergraph by itself has relative codegree
\(\Theta(m^{-2})\), but the one-shot hypergraph obtained by declaring every
deeper target to be another matching vertex has nested cross-rank codegree
\(\Theta(m^{-1})\). Its packet rank is
\(\Theta(m(H-q_0+1))=\Theta(m^{3/2})\). This is an exact reason not to
fold all deeper shadows into an ordinary growing-uniformity matching
argument. They must be treated as correlated cover colors of the entrance
factor.

## 5. Incorporating middle collisions as a slack shore

At rank \(m=n/2\), the intervals in a packet occur in complementary
pairs. Let

\[
 \mathcal P_m
 =\bigl\{\{X,X^c\}:X\in\tbinom{[n]}m\bigr\},
 \qquad |\mathcal P_m|=W/2.
\tag{5.1}
\]

A packet contains exactly \(m\) vertices of \(\mathcal P_m\). Form the
two-shore packet hypergraph \(\mathcal G_R\) whose packet \(\pi\) uses

\[
 E_R(\pi)\ \dot\cup\
 \bigl\{\{I_\pi(j,m),I_\pi(j,m)^c\}:0\le j<m\bigr\}.
\tag{5.2}
\]

A matching in \(\mathcal G_R\) has disjoint entrance targets and no middle
owner collision at all. The latter is stronger than the required
\(o(W)\) collision excess.

### Proposition 5.1 (middle-shore parameters)

Every antipodal middle pair has degree

\[
 d_m=m!^2.
\tag{5.3}
\]

If distinct antipodal pairs are represented by \(X,Y\), and
\(t=|X\cap Y|\), their codegree is

\[
 \mu_m(t)=2\bigl(t!(m-t)!\bigr)^2,
 \qquad 1\le t\le m-1.
\tag{5.4}
\]

Consequently

\[
 \max\frac{\mu_m(t)}{d_m}=\frac{2}{m^2}.
\tag{5.5}
\]

The middle-shore analogue of the conditioned overlap moment is
\(4/m^2+O(m^{-4})\).

#### Proof

Equation (5.3) is Lemma 2.1. The disjoint case at rank \(m\) is the same
antipodal vertex, so distinct quotient vertices have \(t>0\). The union
of representatives has size \(2m-t<n\), and the overlapping-interval
count gives (5.4). Division by \(m!^2\) gives

\[
 \frac{\mu_m(t)}{d_m}=\frac2{\binom mt^2},
\]

whose maximum is at \(t=1,m-1\). The conditioned moment is the sum over
the \(m-1\) other antipodal positions in a fixed packet and is dominated
by the two adjacent positions. \(\square\)

### Proposition 5.2 (cross-shore codegree)

Fix an entrance target \(A\in\binom{[n]}R\) and a middle pair represented
by \(X\in\binom{[n]}m\). Put \(t=|A\cap X|\). Their codegree is

\[
 \nu(t)=
 \begin{cases}
 R!m!(q_0+1)!,&t=0\text{ or }t=R,\\[2mm]
 2(R-t)!t!(m-t)!(q_0+t)!,&1\le t\le R-1.
 \end{cases}
\tag{5.6}
\]

In particular,

\[
 \max_t\frac{\nu(t)}{d_R}
 =\frac{q_0+1}{\binom{m+q_0}{q_0}}
 =\exp\!\left[-\Omega\!\left(q_0\log\frac m{q_0}\right)\right].
\tag{5.7}
\]

#### Proof

Apply Lemma 4.1 with \(a=m,b=R\). Replacing \(X\) by \(X^c\) changes
\(t\) to \(R-t\) and leaves (5.6) unchanged, so the formula is well
defined on antipodal pairs. At the two containment endpoints, division by
\(d_R\) gives

\[
 \frac{m!(q_0+1)!}{(m+q_0)!}
 =\frac{q_0+1}{\binom{m+q_0}{q_0}}.
\]

For \(1\le t\le R-1\), division by \(d_R\) gives

\[
 \frac{2}{\binom Rt\binom{m+q_0}{m-t}},
\tag{5.8}
\]

which is smaller than the endpoint value; the displayed exponential
estimate follows. \(\square\)

Thus the middle constraint has constant global slack and creates no large
cross-shore codegree.

## 6. The exact fractional point and the integral partial-factor attack

Assign every packet the weight \(x_\pi=1/d_R\). Double counting gives

\[
 \sum_{\pi:A\in E_R(\pi)}x_\pi=1
 \qquad(A\in\tbinom{[n]}R),
\tag{6.1}
\]

and total mass

\[
 \sum_{\pi\in\Omega_n}x_\pi
 =\frac{(n-1)!}{R!(n-R)!}
 =\frac1n\binom nR
 =\frac{N_{q_0}}n.
\tag{6.2}
\]

For a middle antipodal pair \(P\), its load is

\[
 \sum_{\pi:P\in E_m(\pi)/\pm}x_\pi
 =\frac{d_m}{d_R}
 =\alpha_m.
\tag{6.3}
\]

Since

\[
 \alpha_m
 =\prod_{i=0}^{q_0-1}\frac{m-i}{m+i+1}
 =e^{-a^2+o(1)},
\tag{6.4}
\]

there is a fixed positive middle slack \(1-\alpha_m\).

This leads to the following exact first integral lemma.

> **Augmented entrance-factor lemma (AEF\(_{a}\), open).** There is a
> matching \(\mathcal M\) in \(\mathcal G_R\) of size
> \(K_0-o(W/m)\) which covers \(N_{q_0}-o(W)\) entrance targets.

AEF would give middle collision mass zero. Adding at most \(o(W/m)\)
arbitrary packets to restore the prescribed packet count can create at
most \(o(W)\) middle collisions and entrance repeats. Thus AEF is already
sufficient for the entrance and middle ledgers.

The exact fluid ledger of a collision-free greedy construction is
favorable. If a fraction \(1-u\) of the entrance targets has been covered,
then the selected packets use

\[
 \frac{(1-u)N_{q_0}}n
\tag{6.5}
\]

packets and hence a fraction

\[
 \alpha_m(1-u)
\tag{6.6}
\]

of the antipodal middle pairs. The middle-free density therefore remains
at least \(1-\alpha_m>0\) throughout. Formulas (0.6), (0.7), (5.5), and
(5.7) give the exact local inputs for a semi-random proof of AEF.

What is not justified is an immediate appeal to a standard fixed-rank
nibble: the packet size in \(\mathcal G_R\) is \(R\)-shore size \(n\)
plus middle-shore size \(m\), hence grows linearly with \(m\). Equation
(3.3) shows the precise borderline in a worst-codegree reduction. The
conditioned moment (3.2) is the extra structure available for a bespoke
proof.

## 7. Deeper ranks are path colors, not a second rounding stage

Let \(s=R-d=m-(q_0+d)\), where \(0\le d\le H-q_0\). Every selected
packet supplies \(n\) targets at rank \(s\). A fixed rank-\(s\) target
has packet degree

\[
 d_s=s!(n-s)!,
\tag{7.1}
\]

and therefore has load under (0.8)

\[
 \ell_d=\frac{d_s}{d_R}
 =\frac{N_{q_0}}{N_{q_0+d}}.
\tag{7.2}
\]

Uniformly for \(q_0\le q\le H\),

\[
 \log\frac{N_{q_0}}{N_q}
 =\frac{q^2-q_0^2}{m}+o(1).
\tag{7.3}
\]

Thus all scalar capacities are at least one and remain bounded by a
constant depending only on \(a,b\).

The correlation is exact. For every \(j\),

\[
 I_\pi(j+d,R-d)
 =\bigcap_{k=0}^{d} I_\pi(j+k,R).
\tag{7.4}
\]

Consequently a chosen rank-\(R\) cycle determines all its deeper lower
targets. Its upper targets are their complements, so the two signs have
identical hole counts. There is no remaining phase or internal compiler
choice after the oriented rank-\(R\) packet has been fixed.

### The exact coordinate-balance invariant

Every coordinate belongs to exactly \(s\) of the \(n\) members of
\(E_s(\pi)\). Consequently every family of \(K\) packets has, at rank
\(s\), exactly \(sK\) occurrence incidences through each coordinate.

Let \(c_s(T)\) be the selected multiplicity of a rank-\(s\) target. Define
the hole family and duplicate multiset by

\[
 \mathcal Z_s=\{T:c_s(T)=0\},
 \qquad
 \mathcal D_s(T)=(c_s(T)-1)_+.
\tag{7.5}
\]

Then, for every coordinate \(x\in[n]\),

\[
 \boxed{
 \deg_{\mathcal D_s}(x)-\deg_{\mathcal Z_s}(x)
 =sK-\binom{n-1}{s-1}
 =\frac{s}{n}\left(nK-\binom ns\right).}
\tag{7.6}
\]

Also

\[
 |\mathcal D_s|-|\mathcal Z_s|=nK-\binom ns.
\tag{7.7}
\]

#### Proof

Count selected rank-\(s\) occurrences containing \(x\). Packetwise the
answer is \(sK\). Relative to the complete rank layer, a hole removes one
incidence and every duplicate copy adds one incidence. Since the complete
layer has coordinate degree \(\binom{n-1}{s-1}\), this proves (7.6).
The unpointed count is identical and gives (7.7). \(\square\)

At the entrance rank, if the packets form a matching, then
\(\mathcal D_R=\varnothing\). With

\[
 \rho=N_{q_0}-nK_0<n,
\]

the leave must therefore be an exactly regular \(R\)-uniform family:

\[
 \boxed{
 |\mathcal Z_R|=\rho,
 \qquad
 \deg_{\mathcal Z_R}(x)=\frac{R\rho}{n}
 \quad(x\in[n]).}
\tag{7.8}
\]

The divisibility \(n\mid R\rho\) is automatic, because
\(n\mid RN_{q_0}\) follows from
\(RN_{q_0}/n=\binom{n-1}{R-1}\). Thus this is not a new scalar Hall cut,
but it shows that an arbitrary leave of size \(\rho\) cannot arise from an
entrance factor.

At deeper ranks, (7.6) is the exact non-scalar ledger an absorber must
respect. In particular the forced duplicate excess cannot be placed
arbitrarily: after subtracting the holes, it must be coordinate-regular.
This constraint is common to all cyclic-order selections and survives every
packet trade.

### The first deeper rank

For \(d=1\), orient each packet's rank-\(R\) trace as a cycle. Its edge

\[
 A\longrightarrow A'
\]

has color \(A\cap A'\in\binom{[n]}{R-1}\). A rank-\(R\) packet matching
is therefore a vertex-disjoint union of directed \(n\)-cycles in the
Johnson graph \(J(n,R)\), and rank \(R-1\) coverage is precisely coverage
of all intersection colors.

A fixed color \(B\in\binom{[n]}{R-1}\) occurs in

\[
 d_{R-1}=(R-1)!(n-R+1)!
\tag{7.9}
\]

catalogue packets, and its fractional load is

\[
 \ell_1=\frac{n-R+1}{R}
 =\frac{m+q_0+1}{m-q_0}
 =1+\Theta(m^{-1/2}).
\tag{7.10}
\]

If exactly \(N_{q_0}\) edge-color occurrences are selected, the unavoidable
repeat excess above the number of available colors is

\[
 \begin{aligned}
 E_1
 &=N_{q_0}-N_{q_0+1}\\
 &=N_{q_0}\frac{2q_0+1}{m+q_0+1}
 =\Theta(W/\sqrt m)=o(W).
 \end{aligned}
\tag{7.11}

If \(h_{q_0+1}\) colors are missing, the actual repeat excess is exactly
\(E_1+h_{q_0+1}\), up to the \(O(m)\) packet-count rounding in (0.3).
Thus the first deeper gate is a near-rainbow cycle-factor problem, not a
new capacity problem.

### General depth

At depth \(d\), each directed \(d\)-edge path of the selected cycle is
colored by the intersection of its \(d+1\) vertices. A target
\(S\in\binom{[n]}{R-d}\) is covered exactly when a selected packet cycle
has a consecutive \((d+1)\)-vertex path inside the up-set of \(S\).
Lemma 4.1 gives every cross-depth pair coefficient needed for a switching
calculation.

An independent or Poisson rounding of the fractional point is unsuitable:
the means \(\ell_d\) in (7.2) stay bounded, so such a rounding has a
positive missing probability at every macroscopic Gaussian depth. The
desired construction must deliberately correlate the path colors. This
is not a conclusion about every integral matching; it is a precise reason
that the fractional marginals and ordinary concentration do not suffice.

## 8. The exact coloured integral programme

For \(s\in\{R-(H-q_0),\ldots,R\}\), a target
\(T\in\binom{[n]}s\), and a packet \(\pi\), put

\[
 a_{s,T}(\pi)=\mathbf 1_{\{T\in E_s(\pi)\}}.
\tag{8.1}
\]

For an antipodal middle pair \(P\), put

\[
 b_P(\pi)=\mathbf 1_{\{P\in E_m(\pi)/\pm\}}.
\tag{8.2}
\]

The strong zero-middle-collision version of the annulus selection problem
is the following integer programme:

\[
 \sum_{\pi}x_\pi=K_0,
 \qquad x_\pi\in\{0,1\},
\tag{8.3}
\]

\[
 \sum_\pi a_{R,A}(\pi)x_\pi\le1
 \qquad(A\in\tbinom{[n]}R),
\tag{8.4}
\]

\[
 \sum_\pi b_P(\pi)x_\pi\le1
 \qquad(P\in\mathcal P_m),
\tag{8.5}
\]

and, with defect variables \(y_{s,T}\in\{0,1\}\),

\[
 \sum_\pi a_{s,T}(\pi)x_\pi+y_{s,T}\ge1
 \qquad(R-H+q_0\le s\le R).
\tag{8.6}
\]

The objective is

\[
 \min\sum_{s=R-H+q_0}^{R}
       \sum_{T\in\binom{[n]}s}y_{s,T}.
\tag{8.7}
\]

Upper targets need no second variables, because complementation maps the
lower occurrence set bijectively to the upper occurrence set in every
packet.

The arithmetic rounding can be included exactly. Put

\[
 \beta=\frac{nK_0}{N_{q_0}}=1-\frac{\rho}{N_{q_0}}
\tag{8.8}
\]

and assign \(x_\pi=\beta/d_R\). This has total mass \(K_0\), entrance
load \(\beta\), and middle-pair load \(\beta\alpha_m<1\). Give every
entrance target fractional defect \(1-\beta\); their total defect is
exactly \(\rho<n\). At every deeper rank,
\(\beta\ell_d\ge1\) for all sufficiently large \(m\), because
\(\ell_d-1=\Omega(m^{-1/2})\) for \(d\ge1\), whereas
\(1-\beta=O(m/W)\). Hence the fractional relaxation has optimum exactly
\(\rho=O(m)=o(W)\). The required theorem is not fractional feasibility
but the following correlated rounding statement.

> **Coloured annulus partial factor (CAPF\(_{a,b}\), open).** The integer
> programme (8.3)--(8.6), or its version allowing \(o(W)\) aggregate
> excess in (8.4)--(8.5), has a solution with objective \(o(W)\).

CAPF gives exactly

\[
 C_0=o(W),\qquad
 \sum_{q=q_0}^{H}h_q=o(W),
\tag{8.9}
\]

with \(K_0=N_{q_0}/(2m)+O(1)\), and therefore gives a literal annulus
compiler of length \(W+o(W)\).

The exact decomposition of CAPF is now clear:

1. AEF is the uncolored augmented partial-factor problem. Its exact local
   parameters are (0.6), (0.7), (5.5), and (5.7).
2. Rank \(R-1\) is a near-rainbow Johnson-cycle factor with forced excess
   (7.11).
3. All larger depths are nested directed-path colors, with mixed-rank
   codegrees (4.1) and coordinate ledger (7.6).
4. Any successful absorber must exchange whole cyclic orders while
   preserving the entrance matching and the middle-pair capacities. A
   post-selection change of packet phase or internal frame cannot alter a
   deeper color.

## 9. Audited boundary

Proved in this note:

1. exact rank-\(q_0\) degrees and every pair codegree;
2. the exact maximum codegree and the sharper conditioned overlap moment;
3. exact unequal-rank codegrees, including the \(2/R\) first nested spine;
4. exact middle-pair and cross-shore parameters;
5. the constant-slack fractional augmented matching;
6. the Johnson edge-color formulation at depth \(q_0+1\), including its
   exact forced repeat ledger; and
7. the exact coordinate-regularity ledger for entrance leaves and deeper
   duplicate-minus-hole multisets; and
8. the all-depth integer programme whose objective is precisely the
   annulus hole sum.

Not proved:

1. AEF for growing packet rank;
2. the near-rainbow completion at the first deeper rank;
3. a nested all-depth absorber; or
4. CAPF and hence coefficient one.

The main positive conclusion is that neither the entrance hypergraph nor
the collision-free middle shore has a degree, codegree, or fractional Hall
defect. The remaining obstruction, if one exists, must be a genuinely
global colored-cycle cut involving the nested path colors. The first place
to search for it is already the rank-\(R-1\) intersection coloring; the
first place a positive proof must go beyond generic matching is a
whole-cycle alternating trade preserving (8.4)--(8.5).
