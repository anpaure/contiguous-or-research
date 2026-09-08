# Promotion rings: exact cycle-catalogue parameters, a custom first bite, and finite-character traps

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad
 \mathcal A_H=\binom{[n]}{m-H},\qquad
 N_H=|\mathcal A_H|,
\tag{0.1}
\]

and let

\[
 W=\binom{2m}m,\qquad \lambda_H=\frac W{N_H}.
\tag{0.2}
\]

We use a calibrated depth with

\[
 H\sim\sqrt{m\log m},\qquad
 1\le \tau:=\frac M{\lambda_H}=1+o(1).
\tag{0.3}
\]

Thus

\[
 T:=MN_H=\tau W=W+E,
 \qquad E=o(W),
 \qquad N_H=\Theta(W/m)=o(W/H).
\tag{0.4}
\]

For every base \(A\in\mathcal A_H\), put

\[
 U_A=[n]\setminus A,\qquad |U_A|=M.
\tag{0.5}
\]

A promotion-ring option is a directed cyclic order \(\pi\) of \(U_A\),
modulo rotation.  Its middle-owner trace is

\[
 \mathcal R(A,\pi)
 =\{A\cup I_\pi(i,H):i\in\mathbb Z_M\},
\tag{0.6}
\]

where \(I_\pi(i,s)\) is the cyclic interval of length \(s\) beginning at
phase \(i\).  Thus one option is a tight Hamilton cycle of the
\(H\)-subsets of \(U_A\) in the standard hypergraph sense: it has one
edge at every cyclic phase, not all \(\binom MH\) possible \(H\)-sets.

The audit has six exact conclusions.

1.  **The ungrouped owner problem has no Hall obstruction.**  Give every
    base \(M\) phase clones and join each clone to every middle owner
    containing the base.  This bipartite graph has a matching which
    saturates all \(W\) middle owners.  Its only unmatched left mass is
    the unavoidable

    \[
                              E=MN_H-W=o(W).
    \tag{0.7}
    \]

    Hence arbitrary owner extensions can be made exact.  The entire
    remaining owner difficulty is requiring the \(M\) extensions of one
    base to be one cyclic-window deck.

2.  **The cycle catalogue has the same favorable local geometry as an
    ordinary packet.**  Every owner has degree

    \[
                    D=\binom mH H!m!=\frac{m!^2}{(m-H)!}.
    \tag{0.8}
    \]

    If two owners have Johnson distance \(d\), their normalized codegree
    is

    \[
      \frac{D(X,Y)}D=
      \begin{cases}
       \displaystyle\frac2{\binom md^2},&1\le d<H,\\[2mm]
       \displaystyle\frac{m-H+1}{\binom mH^2},&d=H,\\[2mm]
       0,&d>H.
      \end{cases}
    \tag{0.9}
    \]

    In particular \(\Delta_2/D=2/m^2\).  More sharply, the total
    codegree mass seen inside one marked ring is

    \[
       \frac1D\sum_{\{X,Y\}\subset\mathcal R(A,\pi)}D(X,Y)
       =\frac{2+o(1)}m.
    \tag{0.10}
    \]

3.  **A custom isolated first bite is valid.**  Mark every catalogue
    option with probability \(p=\gamma/(MD)\), and retain an option only
    when no other marked option shares its base or one of its owners.
    For every fixed small \(\gamma>0\), some outcome retains

    \[
              (1-O(\gamma)-o(1))\frac{\gamma N_H}{M}
    \tag{0.11}
    \]

    base-disjoint, owner-disjoint rings.  This covers a
    \((\gamma+o(1))/M\) fraction of the owner layer.  The influence on a
    fixed owner link is at most \((2+o(1))D/m\), and one-bite link
    fluctuations have Bernstein exponent \(\Theta(m)\).  Thus the two
    adjacent Johnson neighbours do not obstruct a slow, \(M\)-scale
    cycle nibble.

4.  **Arbitrary residual regeneration is false.**  Let

    \[
                         g=\gcd(M,H)=\gcd(m,H).
    \tag{0.12}
    \]

    For a balanced coordinate half \(P\subset[n]\) and a modulus
    \(p\ge2\), Section 6 gives an exact classification of the bases which
    can support a whole ring inside one residue class of
    \(|X\cap P|\pmod p\).  If \(g=1\), no base supports such a ring in
    any single residue class.  Consequently there is a coordinate-balanced
    residual of density \(1/2-o(1)\) when \(m\) is even, and of density
    \(1/3+o(1)\) when \(m\) is odd, which contains no promotion ring at
    all.  This is a statewise finite-character holonomy trap.

5.  **The nested signed flag catalogue is fractionally exact.**  The
    lower and upper depth-\(q\) masks of a phase are

    \[
      A\cup I_\pi(i+q,H-q),
      \qquad
      A\cup I_\pi(i-q,H+q),
    \tag{0.13}
    \]

    up to harmless phase shifts.  A fixed target of either sign has
    catalogue degree

    \[
              D_q=\frac{(m-q)!(m+q)!}{(m-H)!}
                  =D\frac W{N_q},
              \qquad N_q=\binom{2m}{m-q}.
    \tag{0.14}
    \]

    A symmetric tag census with exactly \(N_q\) active phases at threshold
    \(q\) gives load one on every signed target.  Hence neither owners nor
    nested flags have a fractional Hall defect.

6.  **The missing theorem is trajectory-plus-absorption, not another
    degree calculation.**  A successful proof must show that its specific
    slow nibble remains uniform against the finite characters of Section 6,
    and must absorb the final residual by trades involving several bases.
    Independent per-base rings have constant owner-hole density and the
    previously audited \(\Theta(W\sqrt m)\) all-depth floor energy, so
    product heat cannot supply the needed finish.

No complete owner-disjoint ring factor or all-depth colored absorption is
proved here.  What is proved is a custom first bite, the exact marginal
Hall theorem, and the precise arithmetic obstruction which any iteration
must avoid.

## 1. Exact marginal Hall theorem

Replace every base \(A\in\mathcal A_H\) by \(M\) formal phase clones
\((A,j)\), \(j\in[M]\).  Join \((A,j)\) to a middle owner
\(X\in\binom{[n]}m\) exactly when \(A\subset X\).  The clone label does
not affect adjacency.

The containment graph between bases and owners is biregular.  A base has
degree

\[
 d_- =\binom{m+H}H,
\tag{1.1}
\]

and an owner has degree

\[
 d_+=\binom mH.
\tag{1.2}
\]

Their ratio is

\[
                         \frac{d_-}{d_+}
                         =\frac W{N_H}=\lambda_H.
\tag{1.3}
\]

### Theorem 1.1 (exact clone matching)

The phase-clone graph has a matching of size \(W\), saturating every
middle owner.  Equivalently, all but exactly \(E=MN_H-W\) phase clones
can be assigned distinct containing owners.

#### Proof

For a base family \(\mathcal F\subseteq\mathcal A_H\), edge counting in
the biregular containment graph gives

\[
 d_-|\mathcal F|\le d_+|N(\mathcal F)|,
\]

and hence

\[
                         |N(\mathcal F)|\ge
                         \lambda_H|\mathcal F|.
\tag{1.4}
\]

Let \(S\) be any family of phase clones and let \(\mathcal F\) be its
base support.  Then

\[
 |S|-|N(S)|
 \le M|\mathcal F|-\lambda_H|\mathcal F|
 \le(M-\lambda_H)N_H=E.
\tag{1.5}
\]

Hall's deficiency theorem therefore gives a matching of size at least
\(MN_H-E=W\).  The right shore itself has size \(W\), so this is best
possible and saturates it. \(\square\)

The theorem is floor-correct: the full left shore has size \(W+E\), so
its deficiency is exactly \(E\).  It also makes the grouping gap literal.
For a fixed base, the arbitrary matched extensions

\[
                         I=X\setminus A\in\binom{U_A}H
\tag{1.6}
\]

need not be the \(M\) cyclic \(H\)-windows of any order of \(U_A\).

## 2. Exact option degrees and codegrees

There are

\[
                         L=(M-1)!
\tag{2.1}
\]

directed cyclic-order options for a fixed base.  A fixed \(H\)-subset of
an \(M\)-set is a cyclic interval in

\[
                         H!(M-H)!=H!m!
\tag{2.2}
\]

of them.

### Lemma 2.1 (owner degree)

Every middle owner belongs to exactly

\[
                         D=\binom mH H!m!
                          =\frac{m!^2}{(m-H)!}
\tag{2.3}
\]

promotion-ring options.  Moreover

\[
                         \frac LD=\frac{\lambda_H}M
                         =\tau^{-1}.
\tag{2.4}
\]

#### Proof

For an owner \(X\), first choose a base \(A\subset X\) in
\(\binom mH\) ways.  Then \(X\setminus A\) is the prescribed
\(H\)-window in \(U_A\), giving (2.2) choices.  This proves (2.3).
Double counting base-option-owner incidences gives

\[
 N_HLM=WD,
\]

which is (2.4). \(\square\)

### Theorem 2.2 (pair codegrees)

Let \(X,Y\in\binom{[n]}m\) be distinct, with

\[
                         d=|X\setminus Y|=|Y\setminus X|.
\]

If \(1\le d<H\), then

\[
                         \boxed{\frac{D(X,Y)}D
                         =\frac2{\binom md^2}.}
\tag{2.5}
\]

If \(d=H\), then

\[
                         \boxed{\frac{D(X,Y)}D
                         =\frac{m-H+1}{\binom mH^2}.}
\tag{2.6}
\]

If \(d>H\), then \(D(X,Y)=0\).

#### Proof

A common base must satisfy

\[
 A\subset X\cap Y,\qquad |A|=m-H.
\]

For \(d\le H\), the number of such bases is

\[
                         \binom{m-d}{H-d}.
\tag{2.7}
\]

For a fixed common base, the two residual \(H\)-sets in \(U_A\) have
intersection size \(H-d\).  When \(d<H\), the exact two-interval count
is

\[
             2d!^2(H-d)!(m-d)!.
\tag{2.8}
\]

Multiplying (2.7) and (2.8), and dividing by (2.3), gives

\[
 \frac{2d!^2(m-d)!^2}{m!^2}
 =\frac2{\binom md^2}.
\]

When \(d=H\), the residual windows are disjoint and the cyclic block
count is

\[
                         H!^2(m-H+1)!.
\]

There is then one common base.  Division by (2.3) gives (2.6).  No base
exists for \(d>H\). \(\square\)

In particular the maximum normalized codegree is attained at distance
one and equals \(2/m^2\).

## 3. Ring-local overlap mass and bounded influence

Fix an option \(e=\mathcal R(A,\pi)\).  Relative to any one of its
owners, there are exactly two other owners at Johnson distance \(d\), for
each \(1\le d<H\).  The remaining \(M-2H+1\) owners are at distance
\(H\).  Hence Theorem 2.2 gives the following stronger local statistic.

### Proposition 3.1 (exact internal codegree sum)

\[
\begin{aligned}
 \frac1D\sum_{\{X,Y\}\subset e}D(X,Y)
 &=M\sum_{d=1}^{H-1}\frac2{\binom md^2}\\
 &\quad+
 \frac{M(M-2H+1)}2
       \frac{m-H+1}{\binom mH^2}\\
 &=\frac{2+o(1)}m.
\end{aligned}
\tag{3.1}
\]

#### Proof

For \(d<H\), the ring contains exactly \(M\) unordered pairs of windows
at cyclic displacement \(d\).  At distance \(H\), count ordered pairs
from every starting window and divide by two.  This gives the first two
lines.  The \(d=1\) term is \(2M/m^2=(2+o(1))/m\), all \(d\ge2\)
overlapping terms total \(O(m^{-3})\), and the disjoint term is
superpolynomially smaller because \(H\to\infty\) and \(H=o(m)\).
\(\square\)

For an owner \(X\) and an option \(e\not\ni X\), let \(a_X(e)\) be the
number of options through \(X\) which conflict with \(e\), either at a
middle owner or at the base colour.

### Proposition 3.2 (one-option influence)

Uniformly in \(X,e\),

\[
                         a_X(e)\le\left(\frac2m+o(m^{-1})\right)D.
\tag{3.2}
\]

Moreover

\[
                         \sum_ea_X(e)\le(M+2)D^2.
\tag{3.3}
\]

#### Proof

The options through \(X\) meeting \(e\) at an owner are at most

\[
                         \sum_{Y\in e}D(X,Y)
                         \le M\Delta_2
                         =\frac{2M}{m^2}D.
\]

If the base of \(e\) is contained in \(X\), the additional same-base
options through \(X\) number \(H!m!=D/\binom mH=o(D/m)\).  This proves
(3.2).

For (3.3), reverse the count.  Each of the \(D\) options through \(X\)
conflicts with at most \(MD\) options through one of its owners and at
most \(L\le(1+o(1))D\) options through its base. \(\square\)

## 4. A custom isolated first bite

Mark every base-option pair independently with probability

\[
                         p=\frac\gamma{MD},
                         \qquad 0<\gamma<1/10.
\tag{4.1}
\]

Retain a marked option if no other marked option has the same base or a
common middle owner.

### Theorem 4.1 (one-bite extraction)

For every fixed \(\gamma\in(0,1/10)\), there exists a family of
base-disjoint, owner-disjoint promotion rings of size at least

\[
                  \left(1-2\gamma-o(1)\right)
                  \frac{\gamma N_H}{M}.
\tag{4.2}
\]

Consequently one legal bite covers a

\[
                  \left(1-2\gamma-o(1)\right)\frac\gamma M
\tag{4.3}
\]

fraction of all middle owners.

#### Proof

The expected number of marked options is

\[
 N_HLp=N_H\frac LD\frac\gamma M
       =\frac{\gamma\lambda_HN_H}{M^2}
       =(1+o(1))\frac{\gamma N_H}{M}.
\tag{4.4}
\]

Conditional on one option being marked, the expected number of other
marked options sharing one of its owners is at most

\[
                         pMD=\gamma.
\]

The same-base contribution is

\[
                         pL=\frac{\gamma\lambda_H}{M^2}=O(\gamma/M).
\]

The union bound therefore shows that a marked option is isolated with
conditional probability at least \(1-\gamma-O(\gamma/M)\).  Hence the
expected number of isolated options is at least the right side of (4.2),
with room to replace \(\gamma\) by \(2\gamma\) in the error.  Some
outcome attains the expectation.  Isolated options are disjoint on both
resource shores.  Multiplying their number by \(M\), and using
\(MN_H=(1+o(1))W\), proves (4.3). \(\square\)

The bite is deliberately of order \(1/M\).  A constant fraction of bases
cannot be independently activated in one round: a marked ring would then
see \(\Theta(M)\) expected owner conflicts.

There is also genuine one-bite link concentration.  Let \(\xi_e\) be the
marking indicators and put

\[
                         Z_X=\sum_{e\not\ni X}a_X(e)\xi_e.
\tag{4.5}
\]

Propositions 3.2 and (4.1) give

\[
 \operatorname {Var}Z_X
 \le p\max_ea_X(e)\sum_ea_X(e)
 \le\left(\frac{2\gamma+o(1)}m\right)D^2.
\tag{4.6}
\]

Bernstein's inequality therefore yields, uniformly for \(0<\eta\le1\),

\[
 \Pr\bigl(|Z_X-\mathbb EZ_X|>\eta D\bigr)
 \le2\exp\left[-c\frac{m\eta^2}{\gamma+\eta}\right]
\tag{4.7}
\]

for an absolute \(c>0\).  Thus local link degradation is controllable.
What (4.7) does not prove is that the dependent residual after
\(\Theta(M\log(1/\rho))\) slow bites continues to contain legal rings.

Finite-character balance is also inexpensive in one raw bite.  This is
important: the trap in Section 6 is a necessary trajectory invariant, not
evidence that a fresh random bite is biased toward the trap.

### Proposition 4.2 (simultaneous raw character concentration)

Let \(f:\binom{[n]}m\to[-1,1]\), and define

\[
                         Y_f=\sum_e\xi_e\sum_{X\in e}f(X).
\tag{4.8}
\]

Then

\[
 \mathbb EY_f=\frac\gamma M\sum_Xf(X),
 \qquad
 \operatorname {Var}Y_f\le\gamma W,
\tag{4.9}
\]

and

\[
 \Pr(|Y_f-\mathbb EY_f|>t)
 \le2\exp\left[-\frac{t^2}
 {2\gamma W+(2/3)Mt}\right].
\tag{4.10}
\]

Consequently (4.10) holds simultaneously with error \(o(W/M)\) for
every member of any predetermined family of \(\exp(O(m))\) bounded
character tests.  If \(\gamma=o(1)\), discarding nonisolated marks changes
every such statistic by only \(O(\gamma^2W/M)\) in expectation.

#### Proof

Regularity gives the expectation.  Since one option has \(M\) owners,
Cauchy--Schwarz gives

\[
 \left(\sum_{X\in e}f(X)\right)^2
 \le M\sum_{X\in e}f(X)^2.
\]

Summing over options and using owner degree \(D\) yields

\[
 \operatorname {Var}Y_f
 \le pMD\sum_Xf(X)^2
 \le\gamma W.
\]

Each summand has absolute value at most \(M\), so Bernstein proves
(4.10).  Since \(W\) is exponential in \(m\), taking
\(t=o(W/M)\) still makes the exponent dominate \(O(m)\).  Finally,
Theorem 4.1 bounds the expected rejected fraction of marked options by
\(O(\gamma)\); multiplying by the marked owner mass
\(\Theta(\gamma W/M)\) gives the isolation correction. \(\square\)

## 5. Nested shorter-window flags

For a phase \(i\) of \((A,\pi)\), define the lower and upper depth-\(q\)
flags, up to a cyclic shift of the index, by

\[
 L_q(A,\pi,i)=A\cup I_\pi(i+q,H-q),
\tag{5.1}
\]

\[
 U_q(A,\pi,i)=A\cup I_\pi(i-q,H+q),
\tag{5.2}
\]

for \(0\le q\le H\).  They have ranks \(m-q\) and \(m+q\), and are the
intersection and union, respectively, of the appropriate \(q+1\)
consecutive middle owners.

### Theorem 5.1 (exact signed target degrees)

Every fixed target of rank \(m-q\), and every fixed target of rank
\(m+q\), occurs in exactly

\[
                         D_q=\frac{(m-q)!(m+q)!}{(m-H)!}
\tag{5.3}
\]

base-option-phase incidences.  Consequently

\[
                         \frac{D_q}{D}=\frac W{N_q},
                         \qquad N_q=\binom{2m}{m-q}.
\tag{5.4}
\]

#### Proof

Fix \(S\in\binom{[n]}{m-q}\).  Choose a base \(A\subset S\) in
\[
                         \binom{m-q}{H-q}
\]
ways.  Then \(S\setminus A\) is the prescribed interval of length
\(H-q\) in \(U_A\), and the number of cyclic orders containing it is

\[
                         (H-q)!(m+q)!.
\]

Their product is (5.3).  For an upper target of rank \(m+q\), choose
\(A\) in \(\binom{m+q}{H+q}\) ways and prescribe an interval of length
\(H+q\), giving \((H+q)!(m-q)!\) orders.  The product is again (5.3).
Division by (2.3) gives (5.4). \(\square\)

The occurrence in Theorem 5.1 is phase-marked; a prescribed proper
interval determines its phase.  At the degenerate lower endpoint
\(q=H\), all phases of a fixed base give the same target \(A\), so an
SCD-quality construction must activate exactly one tag-\(H\) phase per
base rather than count all phases.

### Corollary 5.2 (exact symmetric tagged fractional point)

Suppose the phase tags have the exact SCD census: across all bases there
are exactly \(N_q\) phases whose tag is at least \(q\), and every base has
exactly one tag-\(H\) phase.  Average uniformly over base cyclic orders,
tag positions, and all placements with that census.  Then every middle
owner has load

\[
                         \tau=\frac{MN_H}W=1+o(1),
\tag{5.5}
\]

while every signed depth-\(q\) target has load exactly one.

#### Proof

Without threshold thinning, the total phase mass at depth \(q\) is
\(MN_H\), uniformly distributed over \(N_q\) targets by Theorem 5.1, so
its load is \(MN_H/N_q\).  The symmetric census activates the fraction
\(N_q/(MN_H)\) of phases at that threshold.  Their product is one.
The owner statement is the case \(q=0\) before the tag thinning. \(\square\)

This fractional point is simultaneous in \(q\): the threshold events are
nested because they arise from one tag at each phase.  It proves that the
shorter-window flags introduce no scalar or fractional Hall deficit.  It
does not control integral cross-base collisions.

## 6. Exact finite-character holonomy

Fix a balanced half

\[
                         P\subset[n],\qquad |P|=m,
\tag{6.1}
\]

and a modulus \(p\ge2\).  Put

\[
 \mathcal U_c^{(p)}(P)
 =\{X\in\tbinom{[n]}m:|X\cap P|\equiv c\pmod p\}.
\tag{6.2}
\]

Recall \(g=\gcd(M,H)=\gcd(m,H)\).

### Theorem 6.1 (complete residue-class classification)

Fix a base \(A\), put \(U=A^c\), and let

\[
                         t=|P\cap U|.
\tag{6.3}
\]

There is a promotion ring of base \(A\) all of whose middle owners lie in
\(\mathcal U_c^{(p)}(P)\) if and only if, for some integer \(k\),

\[
                         t=k\frac Mg
\tag{6.4}
\]

and

\[
                         c\equiv m-k\frac mg\pmod p.
\tag{6.5}
\]

#### Proof

Write a cyclic order of \(U\) in positions \(0,\ldots,M-1\), and put

\[
 b_i=\mathbf1_{\{\pi_i\in P\}}.
\]

The residue of the phase-\(j\) owner is

\[
 |A\cap P|+\sum_{h=0}^{H-1}b_{j+h}\pmod p.
\tag{6.6}
\]

If it is constant in \(j\), consecutive differences give

\[
                         b_{j+H}\equiv b_j\pmod p.
\]

Since \(b_j\in\{0,1\}\) and \(p\ge2\), this is equality.  The shift by
\(H\) on \(\mathbb Z_M\) has \(g\) orbits, each of size \(M/g\).
Thus the one-positions are a union of \(k\) complete orbits, proving
(6.4).

These orbits are the residue classes modulo \(g\).  Every consecutive
\(H\)-interval contains \(H/g\) positions from each orbit, hence
\(kH/g\) one-positions.  Since

\[
 |A\cap P|=m-t=m-kM/g,
\]

the owner intersection count is

\[
 m-kM/g+kH/g=m-km/g,
\]

which proves (6.5).

Conversely, if (6.4) holds, place the labels of \(P\cap U\) in any
\(k\) shift-\(H\) orbits and all other labels in the remaining positions.
Every owner then has the intersection count in (6.5). \(\square\)

### Corollary 6.2 (coprime constant-density trap)

If \(\gcd(m,H)=1\), then no residue class
\(\mathcal U_c^{(p)}(P)\) contains a promotion ring of any base.

If \(m\) is even, one may take a parity class.  It has size

\[
 \frac12\left[W\pm(-1)^{m/2}\binom m{m/2}\right]
 =\left(\frac12+o(1)\right)W
\tag{6.7}
\]

and is an exact ground-coordinate \(1\)-design.

If \(m\) is odd, take the unique \(c\in\mathbb Z_3\) satisfying

\[
                         2c\equiv m\pmod3.
\tag{6.8}
\]

Then \(\mathcal U_c^{(3)}(P)\) has size
\((1/3+o(1))W\), is an exact ground-coordinate \(1\)-design, and contains
no promotion ring.

#### Proof

If \(g=1\), condition (6.4) requires \(t=0\) or \(M\).  But
\(U\) has size \(M>m=|P|\), while its complement \(A\) has size
\(m-H<m\), so

\[
                         H\le t\le m.
\]

Neither endpoint is possible.  This proves ring-freeness.

The parity size follows from

\[
 [z^m](1-z)^m(1+z)^m
 =(-1)^{m/2}\binom m{m/2}.
\]

When \(m\) is even, swapping \(P\) with its complement preserves each
parity class.  Together with permutations inside the two halves this gives
a transitive coordinate automorphism group, proving exact coordinate
balance.

For odd \(m\), the roots-of-unity filter gives asymptotic equidistribution
of \(|X\cap P|\) modulo three.  Condition (6.8) makes the residue class
invariant under the swap \(j\mapsto m-j\), so the same transitive group
proves exact coordinate balance. \(\square\)

For general \(g\), Theorem 6.1 says that only the residue set

\[
 \mathcal S_{g,p}
 =\left\{m-k\frac mg\pmod p:
     H\le k\frac Mg\le m\right\}
\tag{6.9}
\]

can support a whole ring.  Any residue outside \(\mathcal S_{g,p}\) is a
ring-free residual class.  When \(g\) is bounded, choose a fixed modulus
larger than \(|\mathcal S_{g,p}|\); this gives another positive-density
finite-character trap.  For growing \(g\), (6.9), rather than density or
one-coordinate balance alone, is the exact arithmetic statistic a nibble
trajectory must monitor.

## 7. What a valid iteration and absorber must prove

Theorem 4.1 and (4.7) justify a slow custom nibble only at time zero.  A
complete theorem needs the following two additional assertions.

There is a literal local absorption move, but its all-depth cost must be
cancelled rather than summed absolutely.

### Lemma 7.1 (adjacent-transposition atom)

Fix a base \(A\), a tagged cyclic order \(\pi\) of \(U_A\), and let
\(\pi'\) be obtained by swapping two adjacent coordinate labels.  Then:

1. \((A,\pi')\) is another legal promotion ring with the same base and
   the same phase-tag word;
2. its middle-owner deck differs from that of \((A,\pi)\) in exactly two
   deleted and two inserted owners; and
3. at every signed depth \(q\), its active target vector differs in at
   most two deleted and two inserted targets.

Thus the middle \(\ell^1\)-variation is four and the aggregate signed
variation through depth \(H\) is \(O(H)\).  Adjacent-transposition atoms
connect all cyclic-order options of a fixed base.

#### Proof

For any interval length \(1\le s\le M-1\), a cyclic interval is unchanged
by the swap unless it contains exactly one of the two swapped positions.
Only the two intervals whose boundary separates those adjacent positions
can do so.  Hence at most two old sets are replaced by at most two new
sets.  At the middle length \(s=H\), with \(1<H<M-1\), the four sets are
distinct, giving exact variation four.  Restricting to active tagged
phases can only decrease the number affected.  Summing over the lower and
upper lengths proves the variation bound.  Finally, adjacent
transpositions generate every linear order, and hence every cyclic order
modulo rotation. \(\square\)

The atom has enough raw owner capacity.  Since

\[
                         E=O(HN_H),
\tag{7.1}
\]

using \(O(H)\) swaps per base supplies \(O(HN_H)\) owner changes, enough
at the order-of-magnitude level to address the excess \(E\).  If
\(\Theta(E)\) such swaps are needed, summing their flag variations without
cancellation gives only the bound

\[
                         O(HE)=O(H^2N_H)
                         =O\left(\frac{WH^2}{m}\right)
                         =O(W\log m)
\tag{7.2}
\]

at the calibrated depth.  This estimate does not imply \(o(W)\), even
though the true value may be smaller when \(E\) is small or directions
cancel.  Therefore a useful absorber must combine adjacent-swap atoms in
rectangles or longer multi-base trades whose shorter-window directions
cancel at almost every depth.

1. **Character-uniform trajectory.**  Until the owner residual is
   \(o(W)\), and preferably \(o(W/H)\) for the sharp owner leave, every
   base must retain enough cyclic-order options.  The residual must stay
   quantitatively separated from all the classes described by (6.9), as
   well as their intersections and translated versions.  Exact coordinate
   balance is insufficient by Corollary 6.2.

2. **Multi-base colored absorption.**  The final trades must replace
   whole cyclic orders, preserve one option per already fixed base, and
   correct both middle-owner collisions and the nested signed target
   vectors (5.1)--(5.2).  An absorber confined to an unavailable base
   cannot escape a residue trap; the trade must move character mass across
   several bases.

There is a further quantitative warning.  Choosing the ring of every base
independently gives a fixed owner load of mean \(\tau=1+o(1)\), hence a
positive Poisson-scale owner-hole density.  With exact tags, the independent
all-depth floor energy is \(\Theta(W\sqrt m)\).  Therefore an iterative or
absorbing proof must create order-\(W\) owner anticorrelation and
order-\(W\sqrt m)\) signed target anticorrelation.  The exact fractional
point of Corollary 5.2 supplies the marginals but not this covariance.

## 8. Audited boundary

Proved:

1. exact marginal Hall saturation of the middle-owner layer;
2. exact promotion-ring option degrees and all owner pair codegrees;
3. the sharper ring-local overlap moment \((2+o(1))/m\);
4. a legal custom isolated first bite and owner-link concentration;
5. exact lower and upper shorter-window target degrees and a simultaneous
   tagged fractional point; and
6. a connected adjacent-transposition absorption atom with exact
   owner and all-depth variation bounds; and
7. the complete one-character holonomy classification, including a
   constant-density coordinate-balanced ring-free residual when
   \(\gcd(m,H)=1\).

Not proved:

1. iteration of the custom bite to an owner leave \(o(W)\) or
   \(o(W/H)\);
2. a character-preserving residual-regeneration theorem for the actual
   dependent trajectory;
3. a multi-base absorber; or
4. an integral one-cycle-per-base selection with aggregate nested flag
   holes \(o(W)\).

The exact surviving gate is therefore a **colored promotion-ring
resolution with character-controlled trajectory**.  Static Hall,
fractional feasibility, and local Johnson codegrees all pass; arbitrary
residual regeneration fails for the explicit finite-character reason in
Theorem 6.1.
