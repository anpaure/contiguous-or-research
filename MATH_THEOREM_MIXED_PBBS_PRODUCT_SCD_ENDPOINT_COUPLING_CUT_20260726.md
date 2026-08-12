# Mixed PBBS/product-SCD endpoint coupling: the exact Hall inequality and a Gaussian state cut

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input is used.

## 0. Verdict

Let

\[
 q=\lceil A\sqrt m\rceil+1,\qquad A>0\text{ fixed},
 \qquad W_m={2m\choose m}.
\tag{0.1}
\]

The exact product-SCD tail at the corresponding cutoff has positive
Gaussian cost

\[
 \frac{L_m(m-q)}{W_m}\longrightarrow F(A)>0,
\tag{0.1a}
\]

with the harmless index convention \(q=H+1\), while the audited PBBS
compiler has length

\[
 W+O(Bh\sqrt m)=W\bigl(1+O(h/\sqrt m)\bigr)=W+o(W)
\tag{0.1b}
\]

only for \(h=o(\sqrt m)\).  Thus a mixed construction would have to
absorb product-SCD positions into the middle-rank baseline rather than
append them.

The smallest integral condition for doing this is an augmented endpoint
Hall inequality.  If a word of length \(M+e\) covers an \(M\)-set middle
antichain, and \(G^-\), respectively \(G^+\), is the graph of allowed
common-left-endpoint, respectively common-right-endpoint, couplings to a
second rank, then necessarily

\[
 \boxed{
 |\mathcal A|\le |N_{G^-}(\mathcal A)|+e,
 \qquad
 |\mathcal B|\le |N_{G^+}(\mathcal B)|+e
 }
\tag{0.2}
\]

for every lower family \(\mathcal A\) and upper family \(\mathcal B\).
For the endpoint-only relaxation these inequalities are also sufficient.

For the exact product-SCD chain-pair blocks, (0.2) has a linear Gaussian
state obstruction.  Consider two half-cube chains with minimum ranks
\(a>b>0\) satisfying

\[
 a-b\ge q,\qquad 2a+q\le m.
\tag{0.3}
\]

There are two possible block orientations.

* In \(L(C)\Vert R(D)\), the \(q\) displayed canonical rank-\((m+q)\)
  targets have right endpoints at which **no rank-\(m\) interval can
  end**, even if arbitrary letters precede the block.
* In \(L(D)\Vert R(C)\), the \(q\) displayed canonical rank-\((m-q)\)
  targets have starts which admit **no rank-\(m)\) completion inside the
  block**.  Every such start can be completed only by crossing the
  block's outgoing boundary.

Thus no orientation gives a two-sign, same-cell common baseline.  If the
canonical product witnesses are retained, avoiding a literal terminal
endpoint deficit forces the smaller-minimum chain onto the left and
exports the entire \(q\)-step lower completion staircase to the next
block.  The other possible escape is to abandon the affected canonical
upper witnesses altogether.

This is not a sparse phenomenon.  There are

\[
 \Theta_A(4^m/m)
\tag{0.4}
\]

actual chain pairs satisfying (0.3).  Hence the unavoidable local defect
mass is

\[
 \boxed{\Theta_A(q4^m/m)=\Theta_A(W_m).}
\tag{0.5}
\]

Consequently a mixed word of length \(W_m+o(W_m)\) cannot retain the
standard canonical product-SCD boundary witnesses and couple them
cellwise to middle-rank witnesses.  It must reassign or transport
\(\Omega_A(W_m)\) boundary witnesses across product-cell boundaries.
The exact surviving positive statement is therefore a directed
cross-cell staircase matching, stated in Section 7.

The result is a statewise no-go, not a universal impossibility theorem
for mixed words.  A globally rethreaded ordering of chain-pair blocks
could in principle realize the required outgoing staircases.  What is
now excluded is the tempting local claim that the positive fixed-Gaussian
tail cost can be absorbed by independently identifying each product-SCD
block's canonical endpoints with PBBS baseline endpoints.

## 1. Endpoint injection

Let \(Q=(Q_1,\ldots,Q_L)\) be a nonzero literal word.  A witness for a
set \(S\) is an interval \([\ell(S),r(S)]\) such that

\[
 S=\bigcup_{j=\ell(S)}^{r(S)}Q_j.
\tag{1.1}
\]

### Lemma 1.1 (both endpoint maps are injective on an antichain)

If \(\mathcal F\) is an antichain and one witness is chosen for each
member, then both maps

\[
 S\mapsto \ell(S),\qquad S\mapsto r(S)
\tag{1.2}
\]

are injective.

#### Proof

Two intervals with a common left endpoint are nested, so their unions
are comparable.  Distinct members of an antichain are not comparable.
This proves injectivity of the left endpoints.  The right-endpoint proof
is identical. \(\square\)

The lemma applies in particular to every fixed rank.

## 2. The smallest integral coupling inequality

Let \(\mathcal M\) be a middle-rank antichain with
\(|\mathcal M|=M\).  Let \(\mathcal T^-\) and \(\mathcal T^+\) be
lower- and upper-rank antichains.  Fix any collection of allowed witness
states.  Define bipartite graphs

\[
 G^-\subseteq \mathcal T^-\times\mathcal M,
 \qquad
 G^+\subseteq \mathcal T^+\times\mathcal M
\tag{2.1}
\]

as follows:

* \(T\,G^-\,M_0\) when the allowed states contain witnesses for
  \(T\) and \(M_0\) with a common left endpoint;
* \(U\,G^+\,M_0\) when the allowed states contain witnesses for
  \(U\) and \(M_0\) with a common right endpoint.

Shared endpoints automatically impose

\[
 T\subseteq M_0\quad\text{and}\quad M_0\subseteq U,
\tag{2.2}
\]

because the corresponding intervals are nested.

### Theorem 2.1 (augmented endpoint Hall)

Suppose a word of length \(M+e\) realizes all three antichains by the
allowed witness states.  Then, for every
\(\mathcal A\subseteq\mathcal T^-\) and
\(\mathcal B\subseteq\mathcal T^+\),

\[
 |\mathcal A|\le |N_{G^-}(\mathcal A)|+e,
 \qquad
 |\mathcal B|\le |N_{G^+}(\mathcal B)|+e.
\tag{2.3}
\]

Conversely, for one sign at a time, (2.3) is sufficient for the abstract
endpoint assignment obtained by allowing \(e\) additional nonmiddle
endpoint slots.

#### Proof

By Lemma 1.1, the chosen middle witnesses use \(M\) distinct left
endpoints and \(M\) distinct right endpoints.  At most \(e\) word
positions lie outside either middle endpoint set.

For the lower sign, members of \(\mathcal A\) whose starts lie in the
middle start set match injectively to members of
\(N_{G^-}(\mathcal A)\); at most \(e\) other members can start outside
that set.  This proves the first inequality.  Reverse the word to prove
the second.

For sufficiency in the endpoint-only relaxation, adjoin \(e\) dummy
right vertices, adjacent to every target.  Hall's theorem on this
augmented graph is exactly (2.3). \(\square\)

Define the endpoint deficiency

\[
 \operatorname{def}(G)=
 \max_{\mathcal A}\bigl(|\mathcal A|-|N_G(\mathcal A)|\bigr).
\tag{2.4}
\]

Every literal realization therefore has the exact necessary bound

\[
 \boxed{
 e\ge
 \max\{\operatorname{def}(G^-),
       \operatorname{def}(G^+)\}.}
\tag{2.5}
\]

No scalar marginal or fractional averaging statement is a substitute for
(2.3).

## 3. The sub-Gaussian PBBS letters cannot themselves enter the lower annulus

Use the audited PBBS dominance-seam compiler with radius \(K\).  Its
three types of letters obey the following exact lower bounds.

1. An endpoint-capped erosion letter is the intersection of \(K+1\)
   rank-\((m+1)\) Johnson owners, and has size at least
   \(m+1-K\).
2. A lower dominance-staircase letter intersects at most \(2K\)
   consecutive owners, and has size at least \(m+2-2K\).
3. An upper chart letter is an owner and has size \(m+1\).

Consequently every letter in that exact compiler has size at least

\[
 \boxed{m+2-2K.}
\tag{3.1}
\]

If

\[
 q\ge2K-1,
\tag{3.2}
\]

then no interval containing an unchanged PBBS compiler letter can have
union of rank \(m-q\), since its union already contains a set of size
at least \(m+2-2K>m-q\).

For the proved sub-Gaussian theorem one takes \(K=o(\sqrt m)\), while
the first fixed-Gaussian tail rank has
\(q=\lceil A\sqrt m\rceil+1\).  Hence (3.2) eventually holds.  In any
mixed construction preserving those PBBS letters, every lower-annulus
witness lies wholly in a block of new or replaced letters.  Endpoint
sharing must therefore run from the product-SCD blocks into the middle
baseline; the old PBBS positions cannot serve as lower-tail endpoints.

This observation does not forbid replacing PBBS letters.  It identifies
the direction in which a genuine baseline substitution must operate.

## 4. Exact product-SCD block states

Split a \(2m\)-set as \(X\sqcup Y\), with both halves of size \(m\).
Let

\[
 C_a\subset C_{a+1}\subset\cdots\subset C_{m-a},
 \qquad
 D_b\subset D_{b+1}\subset\cdots\subset D_{m-b}
\tag{4.1}
\]

be symmetric chains with \(a,b>0\).  Their increment words are

\[
 R(C)=(C_a,c_{a+1},\ldots,c_{m-a}),
 \qquad L(C)=\operatorname{rev}R(C),
\tag{4.2}
\]

and similarly for \(D\).  Here increment labels denote singleton
letters.  All letters belonging to different halves are disjoint.

In the block

\[
 G_{C,D}=L(C)\Vert R(D),
\tag{4.3}
\]

the set \(C_i\cup D_j\) has the canonical crossing witness consisting
of the suffix of \(L(C)\) with union \(C_i\) and the prefix of \(R(D)\)
with union \(D_j\).  Since \(a,b>0\), this crossing witness has unique
start and end inside the block.

For a lower target \(i+j=m-q\), its canonical start can be shared with a
middle target inside (4.3) exactly when \(D_{j+q}\) exists.  Equivalently,

\[
 j+q\le m-b
 \quad\Longleftrightarrow\quad i\ge b.
\tag{4.4}
\]

For an upper target \(i+j=m+q\), its canonical end can be shared with a
middle target exactly when \(C_{i-q}\) exists.  Equivalently,

\[
 i-q\ge a.
\tag{4.5}
\]

Equations (4.4)--(4.5) are the elementary state transition rules for
the endpoint coupling.

## 5. The two-sign state cut

### Theorem 5.1 (one shore is necessarily defective)

Assume

\[
 a>b>0,\qquad a-b\ge q,qquad 2a+q\le m.
\tag{5.1}
\]

Then the following hold.

#### Forward orientation

In \(G_{C,D}=L(C)\Vert R(D)\), define, for \(0\le k<q\),

\[
 U_k=C_{a+k}\cup D_{m+q-a-k}.
\tag{5.2}
\]

These are \(q\) distinct rank-\((m+q)\) targets.  The right endpoint of
the canonical witness for any \(U_k\) is not the right endpoint of any
rank-\(m\) interval, even in a larger word containing (4.3) as a
contiguous block.

#### Reverse orientation

In \(G_{D,C}=L(D)\Vert R(C)\), define, for \(0\le k<q\),

\[
 T_k=D_{a-q+k}\cup C_{m-a-k}.
\tag{5.3}
\]

These are \(q\) distinct rank-\((m-q)\) targets.  No rank-\(m\) interval
which starts at the canonical start of \(T_k\) can end inside the block.
It must cross the outgoing boundary of \(G_{D,C}\).

#### Proof

The hypotheses give

\[
 a+k\le a+q-1\le m-a,
\]

and

\[
 m+q-a-k\le m-b,
\]

so every set in (5.2) exists.  Its rank is \(m+q\).

Fix its canonical right endpoint in \(R(D)\), whose prefix union is
\(D_j\) with \(j=m+q-a-k\).  An interval ending there and beginning
inside \(R(D)\) has union contained in \(D_j\), of size at most
\(j\le m-b<m\).  If it begins in \(L(C)\), its union is
\(C_t\cup D_j\) for some \(t\ge a\), and hence has size at least

\[
 a+j=m+q-k>m.
\tag{5.4}
\]

If it begins before the block, it contains all of \(L(C)\), so its union
is still larger.  Therefore no rank-\(m\) interval ends at this position.
The \(D_j\)'s, and hence the endpoints, are distinct as \(k\) varies.

For (5.3), the hypotheses give \(a-q+k\ge b\) and
\(m-a-k\in[a,m-a]\), so all targets exist and have rank \(m-q\).
Fix the canonical start with suffix union \(D_{a-q+k}\).  An interval
ending inside \(L(D)\) has rank below \(m\).  If it enters \(R(C)\)
and ends at the prefix with union \(C_t\), then \(t\le m-a\), and its
rank is at most

\[
 (a-q+k)+(m-a)=m-q+k<m.
\tag{5.5}
\]

Thus no middle-rank interval closes before the outgoing block boundary.
The starts are distinct. \(\square\)

The theorem gives an exact dichotomy.  Keeping the larger-minimum chain
on the left creates \(q\) globally dead upper endpoints.  Putting the
smaller-minimum chain on the left removes that terminal obstruction, but
creates a compulsory \(q\)-state lower export across the next block
boundary.

## 6. Gaussian mass of the obstruction

The number of symmetric chains of minimum rank \(a\) in an SCD of
\(Q_m\) is

\[
 A_m(a)={m\choose a}-{m\choose {a-1}}.
\tag{6.1}
\]

For fixed \(x>0\), uniformly for \(x\) in a compact subset of
\((0,\infty)\) and when
\(a=m/2-x\sqrt m+O(1)\), Stirling's formula and the exact subtraction
identity give

\[
 \boxed{
 A_m(a)=
 \left(4x\sqrt{\frac2\pi}e^{-2x^2}+o(1)\right)
 \frac{2^m}{m}.}
\tag{6.2}
\]

Indeed

\[
 A_m(a)={m\choose a}\frac{m-2a+1}{m-a+1},
\tag{6.3}
\]

the binomial factor is

\[
 {m\choose a}=
 \left(\sqrt{\frac2\pi}e^{-2x^2}+o(1)\right)
 \frac{2^m}{\sqrt m},
\tag{6.4}
\]

and the last ratio in (6.3) is \((4x+o(1))/\sqrt m\), with both error
terms uniform on such compact sets.

Choose the fixed windows

\[
 \begin{aligned}
 I_a(m)&=\left\{a:
 A+2\le\frac{m/2-a}{\sqrt m}\le A+3\right\},\\
 I_b(m)&=\left\{b:
 2A+6\le\frac{m/2-b}{\sqrt m}\le2A+7\right\}.
 \end{aligned}
\tag{6.5}
\]

For all sufficiently large \(m\), every \((a,b)\in I_a(m)\times I_b(m)\)
satisfies (5.1) with \(q\) from (0.1).  Also

\[
 a+b\le m-q,
\tag{6.6}
\]

so every such actual chain pair occurs in the exact product-SCD tail at
the boundary rank \(m-q\).

Summing (6.2) over the \(\Theta(\sqrt m)\) integers in each interval gives

\[
 \sum_{a\in I_a(m)}A_m(a)
 =(c_1(A)+o(1))\frac{2^m}{\sqrt m},
\qquad
 \sum_{b\in I_b(m)}A_m(b)
 =(c_2(A)+o(1))\frac{2^m}{\sqrt m},
\tag{6.7}
\]

where

\[
 \begin{aligned}
 c_1(A)&=\int_{A+2}^{A+3}
 4x\sqrt{\frac2\pi}e^{-2x^2}\,dx>0,\\
 c_2(A)&=\int_{2A+6}^{2A+7}
 4x\sqrt{\frac2\pi}e^{-2x^2}\,dx>0.
 \end{aligned}
\tag{6.8}
\]

Hence the number \(N_{m,A}\) of actual chain pairs in this subfamily is

\[
 N_{m,A}=(c_1(A)c_2(A)+o(1))\frac{4^m}{m}.
\tag{6.9}
\]

Each block contributes \(q\) defective states.  If \(N_\to\) blocks use
the forward orientation and \(N_\leftarrow\) use the reverse orientation,
then the upper endpoint deficiency is at least \(qN_\to\), unless those
canonical witnesses are abandoned, while the lower same-cell deficiency
is at least \(qN_\leftarrow\), unless those starts are exported.  Therefore

\[
 \max\{qN_\to,qN_\leftarrow\}
 \ge \frac q2N_{m,A}.
\tag{6.10}
\]

Since

\[
 W_m={2m\choose m}
 =\left(\frac1{\sqrt\pi}+o(1)\right)\frac{4^m}{\sqrt m},
\tag{6.11}
\]

(6.9)--(6.11) give

\[
 \boxed{
 \frac q2N_{m,A}
 =\left(
 \frac{A\sqrt\pi}{2}c_1(A)c_2(A)+o_A(1)
 \right)W_m.}
\tag{6.12}

The coefficient is strictly positive for every fixed \(A>0\).  This is
the exact asymptotic accounting behind (0.5).

For the trimmed odd lift, keep the unstarred copy of these targets and
the rank-\(m\) middle antichain on \(2m+1\) coordinates.  Since

\[
 {2m+1\choose m}\sim2W_m,
\tag{6.13}
\]

the same family still has positive linear density in the odd middle
baseline.  The inserted star cannot repair a dead right endpoint which
occurs before its lift seam, and it cannot reduce an overlarge union.

## 7. The exact surviving cross-cell coupling

The reverse orientation in Theorem 5.1 identifies the only local escape.
At the canonical start of \(T_k\), the union after reading the whole block
is

\[
 B_k=D_{a-q+k}\cup C_{m-a},
 \qquad |B_k|=m-q+k.
\tag{7.1}
\]

Let the next block begin with singleton prefix
\(z_1,z_2,\ldots\), and put \(P_t=\{z_1,\ldots,z_t\}\).  The start of
\(T_k\) becomes a rank-\(m\) baseline start after the next \(q-k\)
letters if and only if

\[
 \boxed{P_{q-k}\cap B_k=\varnothing.}
\tag{7.2}
\]

In that case the shared middle target is exactly

\[
 M_k=B_k\cup P_{q-k}.
\tag{7.3}
\]

The condition is locally feasible: it is enough to choose

\[
 P_q\subseteq[2m]\setminus
       \bigl(C_{m-a}\cup D_{a-1}\bigr),
\tag{7.4}
\]

and the complement in (7.4) has size

\[
 2m-\bigl((m-a)+(a-1)\bigr)=m+1.
\tag{7.5}
\]

Thus there is no one-block cardinality obstruction after the forced
orientation is chosen.  The missing integral theorem is global.

On the Gaussian subfamily (6.5), one has \(a\ge q\) for all sufficiently
large \(m\).  There is then a collision-free local choice: take

\[
 P_q\subseteq X\setminus C_{m-a},\qquad |P_q|=q.
\tag{7.5a}
\]

Every condition (7.2) holds, and the produced middle sets are pairwise
distinct because

\[
 |M_k\cap X|=m-a+q-k
\tag{7.5b}
\]

strictly decreases with \(k\).  Thus even injectivity of the \(q\) local
middle outputs does not obstruct one exported block.  The difficulty is
simultaneously realizing these prefixes as initial portions of distinct
successor product blocks while keeping all outputs globally capacity one.

Form a directed compatibility graph whose left vertices are oriented
chain-pair blocks and whose right vertices are possible successor blocks.
An edge carries an ordered \(q\)-prefix satisfying (7.2), and its
\(q\) labels also determine the \(q\) middle targets in (7.3).  A
coefficient-one mixed construction needs an integral path cover of this
graph such that

1. all but \(o(W_m)\) of the \(\Theta_A(W_m)\) compulsory states in
   (6.12) use a compatible successor edge;
2. the middle targets (7.3) are globally distinct except for
   \(o(W_m)\) losses;
3. the analogous upper right-endpoint assignments satisfy (2.3); and
4. the selected product blocks remain literal and owner-disjoint where
   the construction requires ownership.

Equivalently, for every family \(\mathcal A\) of compulsory outgoing
states, the smallest exact Hall cut is

\[
 \boxed{
 |\mathcal A|
 \le
 \bigl|N_{\rm succ}(\mathcal A)\bigr|+o(W_m),}
\tag{7.6}
\]

where the neighborhood is counted with capacity one on both successor
ports and produced middle targets.  The local estimate (7.5) proves only
positive degree; it does not prove (7.6).

## 8. Precise boundary

The following statements are proved.

1. The endpoint-only integral gate is exactly (2.3).
2. Unchanged sub-Gaussian PBBS compiler letters cannot participate in a
   lower fixed-Gaussian witness.
3. Every imbalanced Gaussian product-SCD block has the two-sign state cut
   of Theorem 5.1.
4. Such blocks carry \(\Theta_A(W_m)\) total defect mass.
5. Therefore independent same-block endpoint identification cannot absorb
   the positive fixed-Gaussian product-tail cost into a coefficient-one
   PBBS baseline.

What is not proved is that the cross-cell system (7.6) fails.  The local
complement size \(m+1\) in (7.5) shows that a purely statewise
cardinality no-go would be false.  A proof of the mixed route must now
construct the capacity-one successor/path assignment in (7.6); a refutation
must give a genuine multi-block Hall witness.  Either result would be
strictly stronger than the separate-tail quantifier and the sub-Gaussian
PBBS theorem.

No coefficient-one conclusion is claimed.
