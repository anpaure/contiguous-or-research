# Corrected annulus intervals: exact overlap hierarchy, matching gate, and deeper-shadow ledger

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or external
input is used.

## 0. Outcome

Put

\[
 n=2m,
 \qquad q_0=\lceil a\sqrt m\rceil,
 \qquad k=m-q_0,
 \qquad V_0=\binom nk,
\tag{0.1}
\]

where \(a>0\) is fixed.  The corrected first-annulus hypergraph
\(\mathcal H_{m,q_0}\) has vertex set \(\binom{[n]}k\).  One edge is the
family of all \(n=2m\) cyclic \(k\)-intervals of a cyclic coordinate
order.

This note proves the following.

1. The simple hypergraph is exactly \(n\)-uniform and regular, with

   \[
                    D={k!(n-k)!\over2}.
   \tag{0.2}
   \]

   If two targets have Johnson distance \(d<k\), their normalized
   codegree is

   \[
        {\lambda_d\over D}
        ={2\over\binom kd\binom{n-k}d}.
   \tag{0.3}
   \]

   For disjoint targets it is

   \[
        {\lambda_k\over D}
        ={2q_0+1\over\binom{n-k}k}.
   \tag{0.4}
   \]

   Hence, for all sufficiently large \(m\),

   \[
       {\Delta_2\over D}={2\over k(n-k)}
       ={2\over m^2-q_0^2}.
   \tag{0.5}
   \]

2. The complete distance-stratum ledger is exceptionally flat.  For a
   fixed target, every non-disjoint Johnson-distance stratum contributes
   total normalized link mass exactly two; the disjoint stratum
   contributes \(2q_0+1\).  Inside one packet, however, the exact
   normalized internal star overlap is only

   \[
   \sigma_{m,q_0}
   ={2\over k(n-k)}+O(m^{-4})
    +\exp[-\Theta(\sqrt m\log m)].
   \tag{0.6}
   \]

   Thus a fresh isolated nibble bite is rigorously efficient in growing
   rank.

3. Consecutive shared targets have a full higher-codegree hierarchy.  A
   prescribed run of \(s+1\) consecutive packet targets has normalized
   common degree

   \[
                {2\over(k)_s(n-k)_s}.
   \tag{0.7}
   \]

   Every further consecutive target therefore costs another
   \(\Theta(m^{-2})\) factor.

4. These time-zero identities do **not** by themselves prove a
   near-perfect integral matching.  They prove a fractional perfect
   matching and an efficient first bite.  Iterating to a leave
   \(o(V_0)\) requires a hereditary residual-regeneration theorem for the
   interval catalogue.  No such theorem is proved here, and a
   fixed-uniformity matching theorem cannot be diagonalized merely from
   (0.5).  Therefore the honest status remains

   \[
   \boxed{\nu^*(\mathcal H_{m,q_0})=V_0,\qquad
          \nu(\mathcal H_{m,q_0})=V_0-o(V_0)
          \text{ is open}.}
   \tag{0.8}
   \]

   Here \(\nu\) and \(\nu^*\) count covered vertices, not packets.

5. A rank-\(q_0\) matching has an exact deeper-shadow ledger.  If
   \(s\ge0\), \(R\) has size \(k-s\), and \(\mu_s(R)\) is the number of
   selected packets in which \(R\) is a cyclic interval, then

   \[
                     (s+1)\mu_s(R)=E_s(R),
   \tag{0.9}
   \]

   where \(E_s(R)\) counts the owned rank-\(k\) interval extensions of
   \(R\) in which \(R\) occupies a consecutive subinterval.  Thus the
   deeper problem is an endpoint/flag-balancing problem on the already
   owned first-rank targets.

6. A quasirandom or independently dispersed packet selection is far from
   enough.  Its natural deeper load at depth
   \(q=x\sqrt m\), \(a\le x\le b\), is

   \[
                         \lambda(x)=e^{x^2-a^2+o(1)}.
   \tag{0.10}
   \]

   Poisson-dispersed loads leave

   \[
   (1+o(1))W\sqrt m
   \int_a^b\exp\{-x^2-e^{x^2-a^2}\}\,dx
   =\Theta_{a,b}(W\sqrt m)
   \tag{0.11}
   \]

   aggregate lower holes.  The desired compiler allows only \(o(W)\).
   Hence a successful matching must be deliberately balanced across all
   deeper interval flags; first-rank disjointness and quasirandomness do
   not propagate coverage.

There are no periodic residues in this labelled annulus problem.  The
only simple/multiple distinction is reversal: a directed order and its
reverse give the same unlabelled interval edge.  Retaining both merely
doubles every degree and codegree.

## 1. Simple and directed catalogues

Let \(\Omega^+\) be the directed cyclic orders of \([n]\), modulo
rotation.  Thus

\[
                         |\Omega^+|=(n-1)!.
\tag{1.1}
\]

For \(\pi\in\Omega^+\), put

\[
 I_\pi(j,k)=\{\pi_j,\pi_{j+1},\ldots,\pi_{j+k-1}\},
 \qquad j\in\mathbb Z_n,
\tag{1.2}
\]

and

\[
                         e(\pi)=\{I_\pi(j,k):j\in\mathbb Z_n\}.
\tag{1.3}
\]

Because the coordinate labels are distinct and \(0<k<n\), the \(n\)
members of (1.3) are distinct.  Reversal of \(\pi\) leaves the set
\(e(\pi)\) unchanged.  For \(2\le k\le n-2\), the interval family
reconstructs the undirected coordinate cycle, so reversal is the only
duplication.  Consequently the simple edge set has size

\[
                         { (n-1)!\over2}.
\tag{1.4}
\]

We use a superscript \(\to\) when the two directions are retained as
parallel labelled edges.  Matching number is determined by the simple
support and is unchanged by this duplication.

## 2. Exact degrees and pair codegrees

### Theorem 2.1 (degree)

Every \(k\)-target has simple degree

\[
                         D={k!(n-k)!\over2},
\tag{2.1}
\]

and directed occurrence degree

\[
                         D^\to=k!(n-k)!.
\tag{2.2}
\]

#### Proof

Contract the prescribed target to one cyclic block.  Order its \(k\)
labels internally and cyclically order the block with the \(n-k\)
outside labels.  This gives \(k!(n-k)!\) directed orders.  Quotient by
reversal for the simple count. \(\square\)

### Theorem 2.2 (pair codegrees)

Let \(S,T\in\binom{[n]}k\) be distinct and put

\[
                         d=|S\setminus T|=|T\setminus S|.
\tag{2.3}
\]

If \(1\le d<k\), then

\[
 \lambda_d
 =d!^2(k-d)!(n-k-d)!,
 \qquad
 \lambda_d^\to
 =2d!^2(k-d)!(n-k-d)!.
\tag{2.4}
\]

If \(d=k\), then

\[
 \lambda_k={k!^2(n-2k+1)!\over2},
 \qquad
 \lambda_k^\to=k!^2(n-2k+1)!.
\tag{2.5}
\]

#### Proof

When \(d<k\), the four nonempty Venn cells occur as four consecutive
blocks in one of the two directions around the coordinate cycle.  Their
internal orders are arbitrary.  The two directions are exchanged by
reversal, giving (2.4).

When \(S,T\) are disjoint, contract each to one block.  Along with the
\(n-2k\) remaining singleton labels, there are \(n-2k+2\) cyclic
objects.  Ordering them cyclically, ordering both blocks internally, and
then quotienting by reversal gives (2.5). \(\square\)

Dividing by (2.1) gives (0.3)--(0.4).  For \(1\le d<k\), write

\[
 M_d=\binom kd\binom{n-k}d.
\tag{2.6}
\]

Then \(M_d\ge k(n-k)\), with equality at \(d=1\), for every sufficiently
large \(m\).  The disjoint ratio in (0.4) is

\[
 {2q_0+1\over\binom{m+q_0}{2q_0}}
 =\exp[-\Theta(\sqrt m\log m)],
\tag{2.7}
\]

so (0.5) follows.

## 3. Distance strata and internal overlap

Fix a target \(S\).  The number of targets at distance \(d\) from it is

\[
                         M_d=\binom kd\binom{n-k}d.
\tag{3.1}
\]

Consequently, for \(1\le d<k\),

\[
 {1\over D}sum_{T:\,d_J(S,T)=d}\lambda(S,T)=2.
\tag{3.2}
\]

At \(d=k\), the same normalized sum is \(2q_0+1\).  Therefore

\[
 {1\over D}sum_{T\ne S}\lambda(S,T)
 =2(k-1)+(2q_0+1)=n-1,
\tag{3.3}
\]

as it must: every packet through \(S\) contains \(n-1\) further targets.

This global link mass is not the parameter seen by an isolated packet
bite.  Fix one packet \(e\) and one \(S\in e\).  Within \(e\), exactly
two intervals lie at each distance \(1\le d<k\), while exactly
\(n-2k+1=2q_0+1\) packet intervals are disjoint from \(S\).  Hence

\[
 {1\over D}\sum_{T\in e\setminus\{S\}}\lambda(S,T)
 =4\sum_{d=1}^{k-1}{1\over M_d}
  +{(2q_0+1)^2\over M_k}.
\tag{3.4}
\]

Define the normalized internal star overlap by

\[
 \sigma(e)={1\over nD}
             \sum_{\{S,T\}\subset e}\lambda(S,T).
\tag{3.5}
\]

Every packet has the same value, and (3.4) gives the exact formula

\[
 \boxed{
 \sigma_{m,q_0}
 =2\sum_{d=1}^{k-1}{1\over
       \binom kd\binom{n-k}d}
  +{(2q_0+1)^2\over2\binom{n-k}k}.}
\tag{3.6}
\]

The \(d=1\) summand is \(2/[k(n-k)]\).  Log-concavity of the binomial
products bounds all \(d\ge2\) terms by \(O(m^{-4})\) in total, apart
from the displayed stretched-exponentially small disjoint term.  This
proves (0.6).

### Theorem 3.1 (consecutive higher codegrees)

Let

\[
 A_i=I_\pi(j+i,k),\qquad 0\le i\le s,
\tag{3.7}
\]

where \(1\le s\le k\).  The simple common degree of these \(s+1\)
targets is

\[
                         d(A_0,\ldots,A_s)
                         =(k-s)!(n-k-s)!,
\tag{3.8}
\]

and hence

\[
 {d(A_0,\ldots,A_s)\over D}
 ={2\over(k)_s(n-k)_s}.
\tag{3.9}
\]

#### Proof

Consecutive targets determine the ordered leaving labels
\(A_i\setminus A_{i+1}\) and entering labels
\(A_{i+1}\setminus A_i\).  In one direction, only the common
\(k-s\) labels and the remaining \(n-k-s\) exterior labels may be
ordered freely.  This gives \((k-s)!(n-k-s)!\) directed realizations in
that direction.  The reverse realization is identified with it in the
simple catalogue.  Conversely every packet containing the chain must
place each adjacent pair at adjacent phases; connectedness forces one
common direction along the entire chain.  Thus there are no further
realizations. \(\square\)

## 4. Fractional factor, fresh bite, and the unresolved trajectory

Give every simple packet weight \(1/D\).  Every target then has load one,
so

\[
                         \nu^*(\mathcal H_{m,q_0})=V_0.
\tag{4.1}
\]

The total fractional packet mass is \(V_0/n\), the information-theoretic
minimum.

There is also a completely uniform first integral bite.  Mark every
packet independently with probability

\[
                         p={\gamma\over nD},
 \qquad 0<\gamma\le1,
\tag{4.2}
\]

and retain a marked packet only if it meets no other marked packet.  If
\(N(e)\) is the number of other packets meeting \(e\), first and second
Bonferroni bounds give

\[
 nD-n-nD\sigma_{m,q_0}
 \le N(e)\le n(D-1).
\tag{4.3}
\]

Therefore

\[
 \Pr(e\text{ is retained})
 ={\gamma e^{-\gamma}\over nD}(1+o(1)).
\tag{4.4}
\]

The retained events for packets through one target are mutually
exclusive.  Summing (4.4) over its \(D\) incident packets shows that each
target is covered with probability

\[
                         {\gamma e^{-\gamma}\over n}(1+o(1)).
\tag{4.5}
\]

Thus some isolated bite covers that fraction of all targets.  This is a
growing-rank statement proved directly from (3.6), with no invocation of
a fixed-rank theorem.

To reach residual density \(\rho\), one would need

\[
                         \Theta(n\log(1/\rho))
\tag{4.6}
\]

successfully regenerated bites.  For example, \(\rho=m^{-1/2}\) would
leave \(V_0/\sqrt m=o(V_0)\) targets and requires
\(\Theta(m\log m)\) bites.

The time-zero calculation does not prove that the residual after a bite
is again nearly regular with internal overlap \(o(1)\).  That hereditary
statement is exactly what is needed for (4.6).  Near-identical coordinate
orders can share \(n-O(1)\) interval targets, so residual propagation
cannot be inferred from pair codegrees alone.  The consecutive hierarchy
(3.9) is favorable evidence, but it is not a proof for arbitrary shared
phase patterns.

Precisely, the following conditional statement is immediate from the
same bite calculation.

> **Residual-regeneration implication.**  If every matching residual of
> density at least \(m^{-1/2}\) contains a spanning subcatalogue which is
> \((1+o(1))D_U\)-regular and has internal overlap \(o(1)\), uniformly in
> the residual, then \(\mathcal H_{m,q_0}\) has a matching covering
> \(V_0-O(V_0/\sqrt m)\) targets.

No proof of the antecedent is presently available.  This is why (0.8),
rather than an unconditional near-factor claim, is the theorem-grade
boundary.

## 5. Exact deeper-shadow identities

Let \(\mathcal M\) be any matching in \(\mathcal H_{m,q_0}\), and put

\[
                         L=|\mathcal M|,
 \qquad \ell=V_0-nL.
\tag{5.1}
\]

Thus \(\ell\) is its uncovered first-rank mass.  For \(s\ge0\), put

\[
 V_s=\binom n{k-s}
     =\binom{2m}{m-q_0-s},
\tag{5.2}
\]

and define

\[
 \mu_s(R)=|\{e\in\mathcal M:R\text{ is a cyclic }(k-s)
                                  \text{-interval of }e\}|.
\tag{5.3}
\]

Every selected packet has exactly \(n\) such intervals, so

\[
                         \sum_R\mu_s(R)=nL=V_0-\ell.
\tag{5.4}
\]

The mean load is

\[
                         \lambda_s={V_0-\ell\over V_s}.
\tag{5.5}
\]

Let

\[
 H_s=|\{R:\mu_s(R)=0\}|,
 \qquad
 C_s=\sum_R(\mu_s(R)-1)_+.
\tag{5.6}
\]

Then the missing/repeat identity is

\[
                         \boxed{H_s=V_s-(V_0-\ell)+C_s.}
\tag{5.7}
\]

This is exact.  It shows that deeper collision excess must be controlled
down to its unavoidable floor \((V_0-\ell)-V_s\).

### Theorem 5.1 (owned-extension identity)

For \(R\in\binom{[n]}{k-s}\), let \(E_s(R)\) count pairs \((S,e)\) such
that

1. \(e\in\mathcal M\);
2. \(S\in e\) is one of its owned rank-\(k\) intervals;
3. \(R\subset S\); and
4. in the cyclic order of \(e\), \(R\) is a consecutive subinterval of
   \(S\).

Then

\[
                         \boxed{E_s(R)=(s+1)\mu_s(R).}
\tag{5.8}
\]

#### Proof

Fix an occurrence of \(R=I_\pi(j,k-s)\) in a selected packet.  The
rank-\(k\) intervals of the same packet which contain it are exactly

\[
                         I_\pi(j-h,k),
 \qquad 0\le h\le s.
\tag{5.9}
\]

These are \(s+1\) distinct owned targets because \(\mathcal M\) is a
rank-\(k\) matching.  Conversely every pair counted by \(E_s(R)\)
recovers the unique occurrence of \(R\) in that packet.  Summing over
packet occurrences proves (5.8). \(\square\)

For \(s=1\),

\[
                         E_1(R)=2\mu_1(R).
\tag{5.10}
\]

Thus every first deeper endpoint count is even, and a target is missing
exactly when its endpoint count is zero.  Moreover

\[
 \frac1{V_1}\sum_RE_1(R)=2\lambda_1
 =2+{4a\over\sqrt m}+o(m^{-1/2})
\tag{5.11}
\]

when \(\ell=o(V_0/\sqrt m)\).  There is only
\(\Theta_a(W/\sqrt m)\) total endpoint slack above the minimum value two
per covered target.  Consequently a successful structured matching must
send endpoint count two to all but \(o(W)\) first-deeper targets; a
generic orientation of the owned extensions cannot suffice.

The exact cross-rank codegree reflects the same fact.  If
\(R\subset S\), \(|R|=k-s\), \(|S|=k\), then

\[
 {d(R,S)\over D}
 ={s+1\over\binom ks}.
\tag{5.12}
\]

Indeed, conditional on \(S\) being a cyclic interval, \(R\) is a
subinterval precisely when the \(s\) deleted labels occupy a total of
\(h\) labels at the left endpoint and \(s-h\) at the right endpoint, for
one of \(s+1\) choices.  Formula (5.12) follows.

## 6. Structured balance and the Poisson hole benchmark

For the structured all-depth target, first assume

\[
                         \ell=o(W/\sqrt m).
\tag{6.0}
\]

This is a convenient strengthening of a bare \(o(V_0)\) first-rank
leave.  The exact scalar necessity is
\(\ell\le V_0-V_1=\Theta_a(W/\sqrt m)\) if the selected occurrence mass
is to dominate \(V_1\); the little-oh form avoids the boundary constant.
For
\(1\le s\le(b-a)\sqrt m+O(1)\), put

\[
                         \alpha_s=\lfloor\lambda_s\rfloor
\tag{6.1}
\]

and define the floor energy

\[
 \Phi_s={1\over2}\sum_R
       (\mu_s(R)-\alpha_s)(\mu_s(R)-\alpha_s-1).
\tag{6.2}
\]

Every summand is a nonnegative integer.  A hole contributes
\(\binom{\alpha_s+1}{2}\), so

\[
                         \boxed{
 H_s\le{\Phi_s\over\binom{\alpha_s+1}{2}}.}
\tag{6.3}
\]

Thus the exact structured matching target is

\[
 \ell+\sum_{s=1}^{(b-a)\sqrt m+O(1)}
 {\Phi_s\over\binom{\alpha_s+1}{2}}=o(W).
\tag{6.4}
\]

It is strictly stronger than a first-rank matching and is sufficient for
\(o(W)\) aggregate lower holes.  Complementation supplies the upper
holes from the same cyclic orders.

There is an equivalent structured-colouring formulation.  Suppose,
strongly, that the simple packet catalogue has a proper edge-colouring

\[
                         \chi:\mathcal P\longrightarrow[D].
\tag{6.4a}
\]

Every rank-\(k\) target has degree \(D\), so every colour then occurs
exactly once at every target.  Thus each colour class is an exact
rank-\(q_0\) factor.  For a deeper target \(R\), let

\[
 J_s(R)=\{\chi(e):R\text{ is a }(k-s)\text{-interval of }e\}.
\tag{6.4b}
\]

Its full-catalogue degree is

\[
 D_s={(k-s)!(n-k+s)!\over2},
 \qquad {D_s\over D}={V_0\over V_s}.
\tag{6.4c}
\]

The aggregate number of depth-\(s\) holes over all \(D\) colour factors
is exactly

\[
 \begin{aligned}
 \sum_{c=1}^D H_s(c)
 &=\sum_R(D-|J_s(R)|)\\
 &=D(V_s-V_0)+
   \underbrace{\sum_R(D_s-|J_s(R)|)}_{\Gamma_s}.
 \end{aligned}
\tag{6.4d}
\]

Here \(\Gamma_s\) is the repeated-colour excess in the deeper target
stars.  Its unavoidable floor is \(D(V_0-V_s)\); equality means that
every colour hits every deeper target.  Thus a proper colouring alone is
not enough.  A colour-balanced resolution with

\[
 \sum_s\bigl[\Gamma_s-D(V_0-V_s)\bigr]=o(DW)
\tag{6.4e}
\]

has some colour class with aggregate deeper holes \(o(W)\).  Conversely,
(6.4d) identifies the exact excess which any proposed structured
resolution must remove.  The existence of the proper \(D\)-colouring
itself is stronger than the open near-factor theorem; this formulation is
a ledger, not an assumed construction.

The Gaussian values are explicit.  Uniformly for
\(s\le(b-a)\sqrt m+O(1)\),

\[
 \lambda_s
 =\exp\left({(q_0+s)^2-q_0^2\over m}+o(1)\right).
\tag{6.5}
\]

In particular, writing \(q_0+s=x\sqrt m+O(1)\),

\[
                         \lambda_s=e^{x^2-a^2+o(1)}.
\tag{6.6}
\]

This constant mean is not enough under diffuse mixing.  As an exact
benchmark, choose

\[
                         L={V_0+o(V_0)\over n}
\tag{6.7}
\]

packets independently and uniformly, ignoring first-rank collisions.  A
fixed depth-\(s\) target belongs to one packet with probability \(n/V_s\),
and hence is missed with probability

\[
 \left(1-{n\over V_s}\right)^L
 =e^{-\lambda_s+o(1)}.
\tag{6.8}
\]

Therefore

\[
 \mathbb EH_s
 =V_s e^{-\lambda_s+o(1)}.
\tag{6.9}
\]

Since

\[
                         {V_s\over W}=e^{-x^2+o(1)},
\tag{6.10}
\]

Riemann summation gives

\[
 \sum_{s=0}^{(b-a)\sqrt m+O(1)}\mathbb EH_s
 =(1+o(1))W\sqrt m
   \int_a^b e^{-x^2-e^{x^2-a^2}}\,dx.
\tag{6.11}
\]

The integral is a strictly positive constant depending only on \(a,b\).
Merely replacing the \(s=0\) histogram by an exact matching histogram,
while leaving the deeper histograms Poisson-dispersed, removes only the
single \(O(W)\) first-rank summand, not the \(W\sqrt m\) scale in (6.11).
Consequently any genuine rank-\(q_0\) matching whose deeper loads remain
asymptotically Poisson still has \(\Theta_{a,b}(W\sqrt m)\) deeper holes.
No assertion is made that conditioning the independent model on being a
matching preserves its law; producing a non-Poisson conditioning is
precisely the live construction problem.

Equation (6.11) is a benchmark, not a universal lower bound on correlated
matchings.  It proves exactly what kind of structure is required: a
successful matching must turn constant-mean Poisson histograms into
floor/ceiling histograms simultaneously at \(\Theta(\sqrt m)\) depths.

## 7. Exact boundary

The corrected annulus hypergraph has no static scalar or pair-codegree
obstruction to a near-perfect first-rank factor.  Its simple/directed
normalizations, full pair codegrees, distance-stratum mass, internal star
overlap, and consecutive higher codegrees are now exact.

The two live integral statements are separate.

1. **First-rank factor:** prove hereditary regeneration, a one-shot
   coloring, or an absorber yielding a matching with leave \(o(V_0)\).
2. **Shadow-balanced factor:** choose such a matching with the energies in
   (6.4) totaling \(o(W)\).

The second does not follow from the first.  Already at \(s=1\), the exact
even endpoint ledger (5.10)--(5.11) demands near-deterministic endpoint
balance.  A successful construction must therefore schedule whole
extension flags or colors, not merely pack the rank-\(q_0\) interval
vertices.
