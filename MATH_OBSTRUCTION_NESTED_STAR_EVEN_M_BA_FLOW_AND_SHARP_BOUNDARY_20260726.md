# Even-rank obstruction to nested-star BA flow, and the sharp approximate boundary

Date: 2026-07-26

Method: exact coordinate dynamics.  No computation, search, or solver is
used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad C=BA,
 \qquad L=m(m+1).
\]

Let \(\mathcal A\) be the labelled catalogue of canonical nested-star
atoms.  An atom has three source states \(I(\alpha)\), three
\(A\)-successor states \(AI(\alpha)\), and six distinct middle owners.
For a Boolean owner-disjoint atom family \(x\), let

\[
 S(x)=\bigcup_{\alpha:x_\alpha=1}I(\alpha).
\]

Its alternating \(BA\)-flow defect is

\[
 d_x=\mathbf 1_{S(x)}-\mathbf 1_{CS(x)}.
\tag{0.1}
\]

The uniform fractional atom point has owner leave zero and \(d_x=0\).
Nevertheless its exact integral rounding is impossible for every even
\(m\).

### Theorem A (exact even-\(m\) integer obstruction)

If \(m\) is even, the only owner-disjoint integral nested-star atom
family with exact \(BA\)-flow is the empty family.  Thus every exact
integral solution has owner leave \(W\), although the uniform
fractional solution has leave zero.

The obstruction does not come from divisibility.  On each \(C\)-orbit,
the source owner at phase \(t+m+1\) is exactly the successor owner at
phase \(t\).  Exact flow activates either every phase of an orbit or no
phase, while owner-disjointness forbids activating both of these phases.

### Theorem B (sharp quantitative form)

For even \(m\), every owner-disjoint integral atom family satisfies

\[
 \boxed{\ \|d_x\|_1\ge {2|S(x)|\over m+1}.\ }
\tag{0.2}
\]

If its owner leave is

\[
 \ell=W-6\sum_\alpha x_\alpha,
\]

then \(|S(x)|=(W-\ell)/2\), and hence

\[
 \boxed{\ \|d_x\|_1\ge {W-\ell\over m+1}.\ }
\tag{0.3}
\]

The coefficient in (0.2) is attained on every individual \(C\)-orbit
at the owner-pair projection.  Therefore (0.3) is the strongest lower
bound obtainable solely from the same-orbit owner collision.  In
particular it is \(\Theta(W/m)=o(W)\) when \(\ell=o(W)\).  It rules out
exact flow but **does not** rule out the approximate target

\[
                 \ell=o(W),\qquad \|d_x\|_1=o(W).
\]

Any claimed impossibility of that approximate target needs an
additional atom-partition or cross-orbit expansion argument.

## 1. The atom packing ILP and its approximate version

For an owner \(X\in\binom{[n]}m\), let

\[
 a_{X\alpha}=\mathbf 1_{\{X\in\Omega(\alpha)\}},
\]

where \(\Omega(\alpha)\) is the set of the six source and successor
owners of \(\alpha\).  For a state \(e\), put

\[
 f_{e\alpha}
 =\mathbf 1_{\{e\in I(\alpha)\}}
  -\mathbf 1_{\{e\in CI(\alpha)\}}.
\tag{1.1}
\]

The exact owner-transversal, alternating-flow ILP is

\[
 \begin{aligned}
  &x_\alpha\in\{0,1\},\\
  &\sum_\alpha a_{X\alpha}x_\alpha=1
       &&\left(X\in\binom{[n]}m\right),\\
  &\sum_\alpha f_{e\alpha}x_\alpha=0
       &&(e\in S_n).
 \end{aligned}
\tag{1.2}
\]

For rounding with leave and signed flow error, replace the owner
equalities by

\[
 u_X:=\sum_\alpha a_{X\alpha}x_\alpha\le1,
 \qquad
 \ell:=\sum_X(1-u_X),
\tag{1.3}
\]

and measure

\[
 \mathfrak D(x)
 :=\sum_e\left|\sum_\alpha f_{e\alpha}x_\alpha\right|.
\tag{1.4}
\]

Because owner-disjointness makes all selected source states distinct,
and also all selected successor states distinct, equations
(0.1) and (1.4) agree:

\[
                    \mathfrak D(x)=|S(x)\triangle CS(x)|.
\tag{1.5}
\]

Each atom has six owners and three sources.  Consequently

\[
 \ell=W-6\sum_\alpha x_\alpha,
 \qquad
 |S(x)|=3\sum_\alpha x_\alpha={W-\ell\over2}.
\tag{1.6}
\]

Every atom already has zero nested Johnson divergence at all protected
depths.  The defect in (1.4) is only the statewise alternating
\(BA\)-flow defect; these two notions must not be conflated.

## 2. Position dynamics and the owner collision

Write a state as \(\pi=(x_1,\ldots,x_n)\).  Directly from the rotor
definitions,

\[
 C\pi=BA\pi=(x_3,x_4,\ldots,x_{n-1},x_1,x_n,x_2).
\tag{2.1}
\]

Thus

\[
 (C\pi)(j)=\pi(\sigma(j)),
\]

where \(\sigma\) has the two position cycles

\[
 (1,3,5,\ldots,2m-1),
 \qquad
 (2,4,6,\ldots,2m,2m+1),
\tag{2.2}
\]

of lengths \(m\) and \(m+1\).  Hence every \(C\)-orbit on permutation
states has length \(L=m(m+1)\).

Let

\[
 P=\{1,2,\ldots,m\},\qquad
 Q=\{2,3,\ldots,m+1\}.
\tag{2.3}
\]

At phase \(t\) of the orbit of \(\pi\), the source and
\(A\)-successor owners are

\[
 X_t=\pi(\sigma^tP),
 \qquad
 Y_t=\pi(\sigma^tQ).
\tag{2.4}
\]

Here and below \(\pi(R)=\{\pi(j):j\in R\}\).

### Lemma 2.1 (exact parity dichotomy)

The sets \(\sigma^tP\), \(t\in\mathbb Z_L\), are all distinct, as are
the sets \(\sigma^tQ\).

If \(m\) is even, then

\[
                     \boxed{Q=\sigma^{m+1}P,}
\tag{2.5}
\]

and this is the unique translate of \(P\) equal to \(Q\).  Hence

\[
                         Y_t=X_{t+m+1}.
\tag{2.6}
\]

If \(m\) is odd, no translate of \(P\) equals \(Q\).

#### Proof

On each cycle in (2.2), the intersection with \(P\) is a nonempty
proper directed interval.  A nonempty proper interval in a cyclically
ordered set has trivial rotational stabilizer.  Therefore
\(\sigma^aP=P\) implies

\[
 a\equiv0\pmod m,
 \qquad
 a\equiv0\pmod{m+1},
\]

and hence \(a\equiv0\pmod L\).  The same proof applies to \(Q\).

Suppose \(m=2r\).  On the odd position cycle, \(P\) consists of its
first \(r\) positions and \(Q\) is its one-step translate.  On the
even position cycle, the two intersections are equal.  Since

\[
 m+1\equiv1\pmod m,
 \qquad
 m+1\equiv0\pmod{m+1},
\]

this proves (2.5).  Uniqueness follows from the trivial stabilizer of
\(P\).

If \(m=2r+1\), then \(P\) contains \(r+1\) positions from the odd
cycle and \(r\) from the even cycle, whereas \(Q\) contains \(r\)
from the odd cycle and \(r+1\) from the even cycle.  Powers of
\(\sigma\) preserve the two cycles, so equality is impossible.
\(\square\)

## 3. Exact integral infeasibility for even \(m\)

Fix one \(C\)-orbit \(O=\{C^t\pi:t\in\mathbb Z_L\}\), and define its
selected phase set

\[
 T_O=\{t:C^t\pi\in S(x)\}\subseteq\mathbb Z_L.
\tag{3.1}
\]

### Lemma 3.1 (owner-disjoint phases)

If \(m\) is even, owner-disjointness implies

\[
                  T_O\cap(T_O+m+1)=\varnothing
\tag{3.2}
\]

for every \(C\)-orbit \(O\).

#### Proof

If both \(t\) and \(t+m+1\) were selected, then the atom containing
the state at phase \(t\) would use its successor owner \(Y_t\), while
the atom containing the state at phase \(t+m+1\) would use its source
owner \(X_{t+m+1}\).  These owners are equal by (2.6), contradicting
(1.3). \(\square\)

#### Proof of Theorem A

Exact flow says \(S(x)=CS(x)\).  Therefore every \(T_O\) is invariant
under translation by one on \(\mathbb Z_L\), and is consequently
either empty or all of \(\mathbb Z_L\).  The full set violates (3.2).
Thus every \(T_O\) is empty, so \(S(x)=\varnothing\), and hence
\(x=0\). \(\square\)

This proves more than failure of a perfect owner transversal: no
nonempty exact integral point exists even when arbitrary owner leave is
allowed.  The corresponding fractional system is nonempty, because
the uniform atom weights satisfy every owner equation and every signed
flow equation by relabelling symmetry.  Hence the obstruction is a
genuine integer-hull obstruction.

## 4. Quantitative approximate boundary

For \(T\subseteq\mathbb Z_L\), let \(r(T)\) be its number of maximal
nonempty cyclic intervals, with \(r(\varnothing)=0\).  If \(T\) is
neither empty nor full, then

\[
             |T\triangle(T+1)|=2r(T).
\tag{4.1}
\]

### Lemma 4.1 (run bound)

Let \(m\) be even, put \(h=m+1\), and suppose

\[
 T\cap(T+h)=\varnothing
 \qquad(T\subseteq\mathbb Z_{mh}).
\tag{4.2}
\]

Then every cyclic interval contained in \(T\) has length at most
\(h\), and

\[
                 |T\triangle(T+1)|\ge {2|T|\over h}.
\tag{4.3}
\]

#### Proof

An interval of length at least \(h+1\) contains two positions whose
difference is \(h\), contrary to (4.2).  Thus
\(|T|\le h r(T)\).  The full set does not satisfy (4.2), so (4.1)
applies whenever \(T\ne\varnothing\), giving

\[
 |T\triangle(T+1)|=2r(T)\ge {2|T|\over h}.
\]

The empty case is immediate. \(\square\)

#### Proof of Theorem B

On the orbit \(O\), the contribution to (1.5) is

\[
 |T_O\triangle(T_O+1)|.
\]

Apply Lemma 4.1 using (3.2), then sum over the disjoint \(C\)-orbits:

\[
 \|d_x\|_1
 =\sum_O|T_O\triangle(T_O+1)|
 \ge {2\over m+1}\sum_O|T_O|
 ={2|S(x)|\over m+1}.
\]

Equation (1.6) gives (0.3). \(\square\)

### Proposition 4.2 (sharpness at the orbit-owner projection)

The constant in (4.3) is exact.  Partition \(\mathbb Z_L\) into the
\(m\) consecutive blocks

\[
 B_j=\{j(m+1),\ldots,(j+1)(m+1)-1\},
 \qquad 0\le j<m,
\]

and put

\[
                         T=\bigcup_{j\ {m even}}B_j.
\tag{4.4}
\]

Then

\[
 T\cap(T+m+1)=\varnothing,
 \qquad
 |T|={L\over2},
 \qquad
 |T\triangle(T+1)|=m={2|T|\over m+1}.
\tag{4.5}
\]

Moreover the \(|T|\) source owners and \(|T|\) successor owners at
these phases are all distinct.

#### Proof

Translation by \(m+1\) sends each block \(B_j\) to \(B_{j+1}\), so
it interchanges selected and unselected blocks because \(m\) is even.
There are \(m/2\) selected blocks, each of length \(m+1\), and each
has two boundary edges, proving (4.5).

Lemma 2.1 says that source owners are distinct among themselves and
successor owners are distinct among themselves.  Its unique cross-role
collision is the shift by \(m+1\), excluded by (4.4). \(\square\)

Proposition 4.2 is deliberately not called an atom construction.  It
shows only that same-orbit owner geometry cannot strengthen (0.3).
Partitioning such phase sets into legal nested-star triples while
avoiding cross-orbit owner collisions is the unresolved global part.

## 5. Arithmetic invariants and the exact boundary

For any integral owner-disjoint atom family,

\[
                        \ell\equiv W\pmod6,
\tag{5.1}
\]

because every atom covers six owners.  If exact flow holds, then
\(S(x)\) is a union of \(C\)-orbits, so

\[
 L\mid |S(x)|={W-\ell\over2}.
\]

Equivalently,

\[
                 W-\ell\equiv0\pmod{2L}.
\tag{5.2}
\]

Thus an exact solution must satisfy

\[
            W-\ell\equiv0\pmod{\operatorname{lcm}(6,2L)}.
\tag{5.3}
\]

These congruences can be repaired by an \(O(m^2)\) leave and therefore
do not obstruct an asymptotic \(o(W)\) leave.  For even \(m\), Theorem
A is the much stronger obstruction: exact flow forces \(\ell=W\).

There are two further exact invariants which become relevant on the
odd-\(m\) branch.  They use the atom structure, not merely the size of
a \(C\)-orbit.

### Proposition 5.1 (endpoint-balance divisibility)

Suppose an integral nested-star atom family has exact \(BA\)-flow, and
let \(N\) be the number of selected full \(C\)-orbits.  Then

\[
                              \boxed{n\mid N.}
\tag{5.4}
\]

More exactly, for every label \(a\), precisely \(mN/n\) of the
selected orbits place \(a\) on the length-\(m\) position cycle in
(2.2).

#### Proof

Let \(r_a\) be the number of selected orbits placing \(a\) on the
length-\(m\) cycle.  In one such orbit, \(a\) occurs in position \(1\)
exactly \(L/m=m+1\) times and never in position \(n\).  In each of the
other \(N-r_a\) orbits it occurs in position \(n\) exactly
\(L/(m+1)=m\) times and never in position \(1\).

Every nested-star atom is an oriented endpoint triangle.  Hence within
each atom every endpoint label occurs equally often in position \(1\)
and in position \(n\).  Summing over the atom family gives

\[
                         (m+1)r_a=m(N-r_a),
\]

or

\[
                         nr_a=mN.
\]

Since \(\gcd(m,n)=\gcd(m,2m+1)=1\), one has \(n\mid N\), and the
stated formula for \(r_a\) follows.  In particular, because
\(W-\ell=2LN\), every exact integral atom circulation also satisfies

\[
                         W-\ell\equiv0\pmod{2Ln}.
\tag{5.4a}
\]

\(\square\)

### Proposition 5.2 (ordered-pair mod-three invariant)

Under the hypotheses of Proposition 5.1, fix distinct labels \(a,b\).
Let \(N_{a\mid b}\) be the number of selected \(C\)-orbits in which
\(a\) lies on the length-\(m\) position cycle and \(b\) lies on the
length-\((m+1)\) position cycle.  Then

\[
                         \boxed{N_{a\mid b}\equiv0\pmod3.}
\tag{5.5}
\]

Equivalently, the sum over selected orbit cuts of their directed cut
matrices is zero modulo three off the diagonal.

#### Proof

In a full \(C\)-orbit there is exactly one phase whose ordered endpoint
pair \((\pi(1),\pi(n))\) equals \((a,b)\) if \(a\) is on the first
position cycle and \(b\) on the second, and there is no such phase
otherwise.  This is the Chinese remainder theorem for the coprime
cycle lengths \(m,m+1\).  Thus the total number of selected source
states with endpoint pair \((a,b)\) is exactly \(N_{a\mid b}\).

For any state \(\pi\), formula (2.1) shows that the final two entries of
the ordered canonical suffix of \(C\pi\) are

\[
                            \pi(1),\pi(n).
\tag{5.6}
\]

Exact flow bijects the selected source set with its \(C\)-image.
Consequently the number of selected sources with endpoint pair
\((a,b)\) equals the number whose ordered suffix ends in \((a,b)\).
But the three sources in every canonical atom have one common ordered
suffix.  The latter count is therefore three times the number of
selected atoms whose common suffix ends in \((a,b)\).  It is divisible
by three, proving (5.5). \(\square\)

In particular the selected orbit cuts form a mod-three
\(2\)-design: if \(r_a\) counts cuts containing \(a\) and
\(s_{ab}\) counts cuts containing both \(a,b\), then

\[
                         r_a-s_{ab}\equiv0\pmod3
                         \qquad(a\ne b).
\tag{5.7}
\]

Applying (5.5) with the reversed pair also gives
\(r_a\equiv r_b\pmod3\).  These are genuine atom-flow congruences,
but they do not by themselves obstruct an \(o(W)\) leave: the required
residue corrections involve only polynomial moduli.

For odd \(m\), Lemma 2.1 shows that one full \(C\)-orbit is internally
owner-simple: its \(L\) source owners and \(L\) successor owners are
all distinct.  Thus the even-rank collision disappears.  Exact flow
would still require many full orbits whose states admit a global
nested-star triple factor.  The ordered-suffix rigidity theorem rules
out a packet supported on only three distinct orbits, but not a growing
cross-orbit incidence network.

The proved boundary is therefore exact:

* exact integral BA-flow is impossible for every even \(m\), despite
  exact fractional feasibility;
* with \(W-o(W)\) owner coverage, even-rank flow error is necessarily
  at least \((1-o(1))W/(m+1)\);
* that forced error is already \(o(W)\), and the orbit-owner projection
  attains it;
* whether legal atom packets can simultaneously achieve
  \(\ell=o(W)\) and \(\mathfrak D=o(W)\) remains a genuinely global
  atom-partition question, not a parity or single-orbit question.
