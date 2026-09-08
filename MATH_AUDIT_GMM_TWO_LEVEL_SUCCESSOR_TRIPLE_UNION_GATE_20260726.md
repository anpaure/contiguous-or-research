# The even-ground two-level successor: source attribution, exact turn collisions, and the unresolved GMM/MS gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Verdict

Assume \(m\ge3\), and put

\[
 \Omega=[2m],\qquad
 {\cal L}=\binom{\Omega}{m-1},\qquad
 {\cal M}=\binom{\Omega}m,\qquad
 {\cal U}=\binom{\Omega}{m+1},
\]

\[
 W=|{\cal M}|,\qquad
 N=|{\cal L}|=|{\cal U}|={m\over m+1}W,\qquad
 D=W-N={W\over m+1}.
 \tag{0.1}
\]

The requested construction-specific estimate is not presently a
well-defined assertion about one object called “the GMM saturating
cycle.”  The source tmp/central/gmlc2.tex proves its Corollary 2 as
follows:

* the case of two consecutive nontrivial levels is imported from
  Mütze--Su, *Bipartite Kneser graphs are Hamiltonian*, Theorem 9;
* the other noncentral cases are imported from earlier work of
  Gregor--Mütze;
* the lexical construction developed in the GMM paper itself concerns
  Hamilton cycles in odd-dimensional central bands and is not an explicit
  successor rule for ranks \(m-1,m\) of \(Q_{2m}\).

Consequently Corollary 2 supplies an existential saturating cycle but does
not select one Mütze--Su Hamiltonian construction, one set of gluing
choices, or one cyclic successor table.  No construction-specific
triple-union count follows from the cited GMM text alone.

For every *specified* saturating cycle, however, the missing statistic has
an exact local normal form.  If

\[
 R_i,X_i,R_{i+1}
 \tag{0.2}
\]

is its chronology, write

\[
 R_{i+1}=R_i-\alpha_i+\beta_i.
 \tag{0.3}
\]

Then its upper colour at \(R_i\) is

\[
 \boxed{
 T_i=R_{i-1}\cup R_i\cup R_{i+1}
    =R_i\cup\{\alpha_{i-1},\beta_i\}.}
 \tag{0.4}
\]

Every collision \(T_i=T_j\) is one of exactly two types:

1. a Johnson-adjacent-lower-set collision with one shared exterior coordinate;
2. a distance-two reciprocal turn.

In particular,

\[
 T_i=T_{i+1}
 \quad\Longleftrightarrow\quad
 \boxed{\beta_{i+1}=\alpha_{i-1}.}
 \tag{0.5}
\]

Thus a linear number of these two-step returns is already a linear
counterexample.  Conversely the desired estimate is exactly equivalent to
saying that only \(o(W)\) positions participate in either of the two
collision types.

The abstract saturating-cycle conclusion does not by itself prove the desired
answer or determine the exact finite defect.  Two explicit valid saturating
cycles in \(J(6,3)\), on the same owner set and both using every lower colour
once, have upper defects four and three.
The known asymptotic GJM lexical collision family is a theorem about a
different four-level lexical forest; it cannot be transferred to the
Mütze--Su/GMM existential cycle.

Accordingly this note neither proves nor refutes

\[
 N-|\{T_i\}|=o(W).
 \tag{0.6}
\]

It isolates one sufficient construction-specific lemma: choose a definite
Mütze--Su successor/gluing rule and prove that the set of positions in the two
collision classes below is \(o(W)\), or exhibit \(\Omega(W)\) pairwise
disjoint such collisions.  A different possible route would be an abstract
extremal theorem showing that some saturating cycle has small defect without
specifying the recursive successor rule.

## 1. What GMM Corollary 2 actually selects

The relevant passage of tmp/central/gmlc2.tex first states that every
sequence of consecutive cube levels has a saturating cycle and a tight
enumeration.  Its proof then treats the saturating-cycle case \(\ell=2\)
separately: apart from the trivial boundary levels, it invokes
Mütze--Su, Theorem 9.  Only the remaining cases are referred to the earlier
trimming-and-gluing theorems.

This has two consequences.

### Proposition 1.1 (there is no GMM two-level successor datum)

The statement of GMM Corollary 2, and its proof inside gmlc2.tex, do not
define maps

\[
 R\longmapsto R^+,\qquad
 R\longmapsto(\alpha(R),\beta(R))
 \tag{1.1}
\]

on \({\cal L}\).  In particular they do not define a canonical multiset
\(\{T_i\}\).

#### Proof

The corollary is existential.  In the two-level case its proof consists of
the cited implication from Mütze--Su, with no reproduction of that
construction and no fixing of its Hamilton-cycle or gluing choices.  The
successor data (1.1) therefore occur neither in the corollary's statement
nor in its proof. \(\square\)

This is a quantifier issue, not a bibliographic nicety.  For each \(m\), let
\({\cal S}_m\) be the set of simple cycles saturating the lower shore, and put

\[
 d_m(C)=N_m-|\{T_i(C)\}|.
 \tag{1.2}
\]

Corollary 2 says only that \({\cal S}_m\ne\varnothing\).  The positive
upgrade needed here is the family-level assertion

\[
 \boxed{\min_{C\in{\cal S}_m}d_m(C)=o(W_m),}
 \tag{1.3}
\]

equivalently, there is a sequence \(C_m\in{\cal S}_m\) with
\(d_m(C_m)/W_m\to0\).  In fully expanded quantifiers, for every
\(\varepsilon>0\) there must be \(m_0\) such that, for every \(m\ge m_0\),
some \(C\in{\cal S}_m\) satisfies \(d_m(C)\le\varepsilon W_m\).  The
nonemptiness supplied by Corollary 2 does not imply (1.3); proving that
upgrade is precisely the new theorem under attack.

## 2. Exact direction-word formula

Fix henceforth any simple saturating cycle

\[
 R_0,X_0,R_1,X_1,\ldots,R_{N-1},X_{N-1},R_0
 \tag{2.1}
\]

in the inclusion graph between \({\cal L}\) and \({\cal M}\).  All
indices are cyclic.  Since consecutive lower sets are distinct facets of
the same \(m\)-set, there are unique coordinates

\[
 \alpha_i\in R_i\setminus R_{i+1},\qquad
 \beta_i\in R_{i+1}\setminus R_i
 \tag{2.2}
\]

such that (0.3) holds.  Moreover,

\[
 X_i=R_i\cup\{\beta_i\}
    =R_{i+1}\cup\{\alpha_i\}.
 \tag{2.3}
\]

### Lemma 2.1 (turn-pair formula)

Define the unordered turn pair

\[
 \tau_i=\{\alpha_{i-1},\beta_i\}.
 \tag{2.4}
\]

Then \(\tau_i\subseteq\Omega\setminus R_i\), its two entries are distinct,
and

\[
                         T_i=R_i\cup\tau_i.             \tag{2.5}
\]

#### Proof

The incoming owner is

\[
 X_{i-1}=R_i\cup\{\alpha_{i-1}\},
\]

and the outgoing owner is

\[
 X_i=R_i\cup\{\beta_i\}.
\]

Both added coordinates lie outside \(R_i\).  If they were equal, then
\(X_{i-1}=X_i\), contradicting simplicity of (2.1).  Taking the union
proves (2.5). \(\square\)

Thus the triple-union problem is a turn-correlation problem for the
deletion/insertion word, not a marginal property of the lower Hamilton
cycle.

## 3. Complete classification of pair collisions

### Theorem 3.1 (two collision types)

Let \(i\ne j\).  Then \(T_i=T_j\) if and only if exactly one of the
following holds.

**Type I: Johnson-adjacent lower sets.**  There are an \((m-2)\)-set \(C\) and
distinct \(p,q,z\notin C\) such that

\[
 R_i=C\cup\{p\},\qquad R_j=C\cup\{q\},
 \tag{3.1}
\]

\[
 \tau_i=\{q,z\},\qquad\tau_j=\{p,z\}.
 \tag{3.2}
\]

In this case

\[
                         T_i=T_j=C\cup\{p,q,z\}.        \tag{3.3}
\]

**Type II: distance-two reciprocal turns.**  There are an
\((m-3)\)-set \(C\) and four distinct points \(p,q,r,s\notin C\) such
that

\[
 R_i=C\cup\{p,q\},\qquad R_j=C\cup\{r,s\},
 \tag{3.4}
\]

\[
 \tau_i=\{r,s\},\qquad\tau_j=\{p,q\}.
 \tag{3.5}
\]

In this case

\[
                         T_i=T_j=C\cup\{p,q,r,s\}.      \tag{3.6}
\]

#### Proof

Suppose \(T_i=T_j=T\).  By Lemma 2.1,

\[
                         R_i=T\setminus\tau_i,\qquad
                         R_j=T\setminus\tau_j,          \tag{3.7}
\]

where \(\tau_i,\tau_j\) are distinct two-subsets of \(T\), because
\(R_i\ne R_j\).  Two distinct two-subsets intersect in either one or zero
points.

If they intersect in \(z\), write

\[
 \tau_i=\{q,z\},\qquad\tau_j=\{p,z\}.
\]

Then \(C=T\setminus\{p,q,z\}\) gives (3.1)--(3.3).

If they are disjoint, write

\[
 \tau_i=\{r,s\},\qquad\tau_j=\{p,q\}.
\]

Then \(C=T\setminus\{p,q,r,s\}\) gives (3.4)--(3.6).

The reverse implications follow immediately by taking the displayed
unions. \(\square\)

In particular collision testing never requires comparing arbitrary
distant lower sets: only Johnson distance one and two can contribute.

### Corollary 3.2 (adjacent collision equals a two-step return)

Equation (0.5) holds.

#### Proof

From (0.3),

\[
\begin{aligned}
 T_i&=R_i\cup\{\alpha_{i-1},\beta_i\},\\
 T_{i+1}
 &=R_{i+1}\cup\{\alpha_i,\beta_{i+1}\}\\
 &=R_i\cup\{\beta_i,\beta_{i+1}\}.
\end{aligned}
 \tag{3.8}
\]

The common coordinate \(\beta_i\) is outside \(R_i\), and
\(\alpha_{i-1}\notin R_i\).  Also \(\beta_{i+1}\notin R_i\): otherwise
\(\beta_{i+1}=\alpha_i\), the unique member of \(R_i\setminus R_{i+1}\),
and then \(X_i=X_{i+1}\), contrary to simplicity.  Simplicity also
excludes \(\alpha_{i-1}=\beta_i\), while
\(\beta_{i+1}\ne\beta_i\) because \(\beta_i\in R_{i+1}\).  Equality of the two
\((m+1)\)-sets is therefore equivalent to
\(\alpha_{i-1}=\beta_{i+1}\). \(\square\)

## 4. Exact defect and pair-collision ledgers

For \(T\in{\cal U}\), put

\[
 u(T)=|\{i:T_i=T\}|,
 \qquad
 R^+=\sum_T(u(T)-1)_+=N-|\{T_i\}|.
 \tag{4.1}
\]

Let

\[
 {\cal B}=\{i:\text{there is }j\ne i\text{ with }T_j=T_i\}
 \tag{4.2}
\]

be the set of collision-participating positions, and let

\[
 \Pi=\sum_T\binom{u(T)}2.
 \tag{4.3}
\]

### Theorem 4.1 (equivalent bad-position form)

\[
 \boxed{
 R^+\le |{\cal B}|\le2R^+.}
 \tag{4.4}
\]

Consequently

\[
                         R^+=o(W)
 \quad\Longleftrightarrow\quad
                         |{\cal B}|=o(W).              \tag{4.5}
\]

Furthermore,

\[
 \boxed{
 R^+\le\Pi\le {m\over2}R^+.}
 \tag{4.6}
\]

The quantity \(\Pi\) is exactly the number of unordered Type-I and Type-II
pairs in Theorem 3.1.

#### Proof

For one target of load \(k\ge2\), its contribution to
\((R^+,|{\cal B}|,\Pi)\) is

\[
                         (k-1,k,\binom k2).
 \tag{4.7}
\]

Thus \(k-1\le k\le2(k-1)\) and \(k-1\le\binom k2\).

It remains to bound \(k\).  The \(m\)-subsets contained in a fixed
\((m+1)\)-set \(T\) form a clique of order \(m+1\) in \(J(2m,m)\).
The edges of the projected simple cycle carrying colour \(T\) form the
subgraph of the projected cycle induced on the owners contained in \(T\).
That subgraph has maximum degree two.
It cannot contain a cycle component unless it is the entire projected
cycle, which is impossible because \(N>m+1\).  It is therefore a union of
paths on at most \(m+1\) vertices and has at most \(m\) edges.  Hence
\(k\le m\), and

\[
 \binom k2\le {m\over2}(k-1).
\]

Summing proves (4.4)--(4.6).  The final assertion is Theorem 3.1.
\(\square\)

### Corollary 4.2 (linear-return obstruction)

Let

\[
 A=\bigl|\{i:\beta_{i+1}=\alpha_{i-1}\}\bigr|.
 \tag{4.8}
\]

Then

\[
                         R^+\ge A.                    \tag{4.9}
\]

In particular, \(A=\Omega(W)\) refutes the desired estimate for that
specified successor rule.

#### Proof

By Corollary 3.2, \(A\) is the number of equal adjacent pairs in the cyclic
word \(T_0,\ldots,T_{N-1}\).  This word is not constant: otherwise every
\(R_i\) would be an \((m-1)\)-subset of one fixed \((m+1)\)-set, allowing
at most \(\binom{m+1}2<N\) distinct lower vertices.

Decompose the cyclic word into maximal constant runs.  If there are \(r\)
runs, then \(A=N-r\), while the number of distinct letters is at most
\(r\).  Therefore

\[
 R^+=N-|\{T_i\}|\ge N-r=A.
\]

\(\square\)

The converse of Corollary 4.2 is false: distant Type-I collisions and
Type-II reciprocal turns may remain even when \(A=0\).

### Proposition 4.3 (independent-turn pseudorandomness has linear defect)

This proposition is a comparison model, not a cycle construction.  For
each \(R\in{\cal L}\), independently choose

\[
 \tau(R)\in\binom{\Omega\setminus R}{2}
 \tag{4.10}
\]

uniformly, and put \(T(R)=R\cup\tau(R)\).  Let

\[
                         K=\binom{m+1}{2}.
 \tag{4.11}
\]

Then

\[
 \mathbb E\!\left[N-|\{T(R):R\in{\cal L}\}|\right]
 =N\left(1-{1\over K}\right)^K
 =\left(e^{-1}+o(1)\right)N,
 \tag{4.12}
\]

and

\[
 \mathbb E\sum_{T\in{\cal U}}\binom{u(T)}2
 =N\,{K-1\over2K}
 =\left({1\over2}+o(1)\right)N.
 \tag{4.13}
\]

#### Proof

Fix \(T\in{\cal U}\).  It has exactly \(K\) rank-\((m-1)\) subsets
\(R\).  For each such \(R\),

\[
                         T(R)=T
 \quad\Longleftrightarrow\quad
                         \tau(R)=T\setminus R,
\]

an event of probability \(1/K\).  These events are independent for the
different \(R\)'s.  Therefore

\[
                         u(T)\sim\operatorname {Bin}(K,1/K).
 \tag{4.14}
\]

Since \(\mathbb Eu(T)=1\),

\[
 \mathbb E(u(T)-1)_+
 =\mathbb Eu(T)-\Pr(u(T)\ge1)
 =\left(1-{1\over K}\right)^K.
\]

Summing over the \(N\) upper targets proves (4.12).  Also

\[
 \mathbb E\binom{u(T)}2
 =\binom K2K^{-2}={K-1\over2K},
\]

which proves (4.13). \(\square\)

Thus an argument saying merely that the two turn coordinates are locally
uniform or pseudorandom points in the wrong direction: independent local
turns have Poisson-scale, hence linear, upper holes.  A positive
construction needs a near-permutation correlation between the \(N\) lower
turns and the \(N\) upper targets.  The proposition does not refute the
Mütze--Su cycle because its turns are highly dependent.

## 5. Owner-leave point law

Let

\[
 {\cal E}={\cal M}\setminus\{X_0,\ldots,X_{N-1}\},
 \qquad |{\cal E}|=D,
 \tag{5.1}
\]

and let \(d_{\cal E}(v)\) count omitted owners containing \(v\).

### Proposition 5.1 (exact point margin)

For every \(v\in\Omega\),

\[
 \boxed{
 \sum_{\substack{T\in{\cal U}\\v\in T}}(u(T)-1)
     =D-2d_{\cal E}(v).}
 \tag{5.2}
\]

#### Proof

For every projected Johnson edge with lower colour \(R\), upper colour
\(T\), and endpoints \(X,Y\), one has

\[
                         {\bf1}_R+{\bf1}_T
                         ={\bf1}_X+{\bf1}_Y.           \tag{5.3}
\]

Sum over the cycle.  Every lower colour occurs once and every used owner
has degree two, so

\[
 d_{\cal L}(v)+\sum_{T\ni v}u(T)
 =2\left({W\over2}-d_{\cal E}(v)\right).
 \tag{5.4}
\]

The baseline identity

\[
                         d_{\cal L}(v)+d_{\cal U}(v)=N=W-D
 \tag{5.5}
\]

gives (5.2) after subtracting one occurrence of every upper target.
\(\square\)

This is a necessary construction-specific audit, but it cannot decide the
asymptotic gate by itself.  Since \(|{\cal E}|=D=O(W/m)\), each coordinate
margin in (5.2) is \(O(D)\).  Across all \(2m\) coordinates, however, the
aggregate \(\ell^1\) discrepancy can be \(O(mD)=O(W)\).  Linear upper
collision mass may therefore have perfectly balanced point margins.

## 6. Abstract saturation does not determine the defect

At \(m=3\), consider the two cyclic owner lists

\[
\begin{aligned}
 C_{\rm old}=(&126,236,136,156,125,256,456,245,234,123,\\
              &135,345,346,146,124),\\
 C_{\rm new}=(&126,136,236,256,125,156,456,245,234,123,\\
              &135,345,346,146,124).
\end{aligned}
 \tag{6.1}
\]

Their cyclic lower-intersection lists are

\[
\begin{aligned}
 &(26,36,16,15,25,56,45,24,23,13,35,34,46,14,12),\\
 &(16,36,26,25,15,56,45,24,23,13,35,34,46,14,12).
\end{aligned}
 \tag{6.2}
\]

Each line is exactly \(\binom{[6]}2\), so both are valid simple
two-level saturating cycles.

Their upper lists are

\[
\begin{array}{c|lllllllllllllll}
 C_{\rm old}
 &1236&1236&1356&1256&1256&2456&2456&2345&1234&1235
 &1345&3456&1346&1246&1246\\
 C_{\rm new}
 &1236&1236&2356&1256&1256&1456&2456&2345&1234&1235
 &1345&3456&1346&1246&1246.
\end{array}
 \tag{6.3}
\]

The first support has size \(11\) and the second size \(12\).  Since
\(N=15\),

\[
                         R^+(C_{\rm old})=4,\qquad
                         R^+(C_{\rm new})=3.           \tag{6.4}
\]

All displayed verifications are literal set identities.  Hence the
lower-saturation property alone neither fixes the triple-union histogram
nor makes it invariant under legal lower-preserving cycle switches.

This finite certificate does not prove a linear asymptotic obstruction, nor
does it exclude a universal \(o(W)\) upper bound for every saturating cycle.
Its exact role is to prove non-invariance of the finite histogram.  A
construction-specific analysis of a selected successor rule is one
sufficient route; an abstract extremal theorem over all saturating cycles is
another.

## 7. Why the GJM lexical collision theorem does not answer this question

The audited GJM collision injection concerns a lower lexical forest from a
four-central-level construction.  Its edge is indexed by a binary word
\(x\) of length \(2m+1\) and weight \(m-1\), and its opposite colour is
obtained by changing the last two down-steps in the lexical row scan.
That map has a disjoint collision family of size

\[
 \binom{2m-1}{m-2}
   =\left({1\over4}-o(1)\right)\binom{2m+1}m.
 \tag{7.1}
\]

This does not evaluate (0.4):

1. it uses a different ground size and a different collection of levels;
2. it is a fixed lexical forest, not the cyclic turn word of a
   Mütze--Su two-level saturating cycle;
3. its upper-level six-cycle joins leave that forest unchanged, whereas
   the current statistic depends on both the incoming and outgoing
   direction at every lower vertex.

Therefore (7.1) is a rigorous no-go for the GJM backbone and no more.  It
must not be reported as a collision theorem for the Corollary 2
saturating cycle.

## 8. A sufficient construction-specific lemma

One direct route through the even-ground GMM/MS construction is to fix, for
every \(m\), one definite cycle among those supplied through the Mütze--Su
construction, including all recursive gluing choices.  Let
\((\alpha_i,\beta_i)\) be its induced direction word.

The exact positive target is

\[
 \boxed{
 \left|\left\{i:\exists j\ne i,\ 
 R_i\cup\{\alpha_{i-1},\beta_i\}
 =
 R_j\cup\{\alpha_{j-1},\beta_j\}
 \right\}\right|=o(W).}
 \tag{8.1}
\]

By Theorem 3.1, the quantified pairs in (8.1) need only be checked at
Johnson distance one and two.  By Theorem 4.1, (8.1) is equivalent to the
desired triple-union estimate.

The sharp negative alternative is a family of \(\Omega(W)\) positions,
paired disjointly into Type-I or Type-II collisions.  The easiest possible
certificate is already

\[
 |\{i:\beta_{i+1}=\alpha_{i-1}\}|=\Omega(W),
 \tag{8.2}
\]

by Corollary 4.2.

No successor formula or gluing distribution available in the GMM
Corollary 2 source proves either (8.1) or (8.2).  This is the exact barrier
for the construction-specific route.  Alternatively one could prove the
abstract minimum-defect assertion (1.3), without selecting a canonical
successor.  Neither route is supplied by the existential corollary, and one
must not replace either by an unverified claim that the published cycle is
pseudorandom.
