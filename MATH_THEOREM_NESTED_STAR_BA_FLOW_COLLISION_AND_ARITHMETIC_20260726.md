# Nested-star atoms: the even-\(m\) \(BA\)-collision, exact arithmetic, and the critical approximate-flow scale

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or
external input is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad W=\binom n m=(2m+1)\operatorname {Cat}_m,
 \qquad L=m(m+1).
\]

Consider an owner-disjoint family of labelled nested-star atoms.  If
there are \(a\) atoms, let \(S\subset S_n\) be their \(3a\) source
states and let

\[
 \ell=W-6a
\]

be the number of unused middle owners.  Write \(C=BA\), and measure its
signed flow defect by

\[
 d_S(\pi)={\bf1}_S(\pi)-{\bf1}_S(C^{-1}\pi),\qquad
 \Delta_{BA}(S)=\frac12\lVert d_S\rVert _1.
\tag{0.1}
\]

This note proves four exact conclusions.

1. **There is a parity-dependent owner collision.**  If \(m\) is even,
   then for every state π

   \[
                  X(C^{m+1}\pi)=X(A\pi).
   \tag{0.2}
   \]

   Owner-disjointness consequently forces

   \[
                  S\cap C^{m+1}S=\varnothing.
   \tag{0.3}
   \]

   In particular a nonempty integral nested-star packing can never
   have exact \(BA\)-flow when \(m\) is even.

2. The robust form of this collision is

   \[
   \boxed{
   \lVert d_S\rVert _1\ge {W-\ell\over m+1},\qquad
   \Delta_{BA}(S)\ge {W-\ell\over2(m+1)}.}
   \tag{0.4}
   \]

   The coefficient and scale in (0.4) are sharp for a single
   \(BA\)-orbit while retaining all source/successor owner inequalities.
   Thus even-\(m\) exact flow is closed, and any proposed rounding must
   pay order \(W/m\) signed defect.  Since \(W/m=o(W)\), this does **not**
   refute the weaker target in which both the owner leave and signed
   defect are merely \(o(W)\).

3. If exact \(BA\)-flow is imposed (for any \(m\)), every unused-owner
   degree is divisible by \(m\).  Exact owner coverage would require

   \[
                     \boxed{2m(m+1)\mid\operatorname {Cat}_m.}
   \tag{0.5}
   \]

   In particular (0.5) fails for every odd prime \(m=p\), because
   \(\operatorname {Cat}_p\equiv2\pmod p\).  This is stronger than the
   total orbit-length divisibility alone.

4. None of these congruences gives an \(o(W)\)-level obstruction.  The
   integer \(BA\)-incidence matrix has torsion-free cokernel on every
   orbit.  An arbitrary orbit-cardinality residue can be created by
   only two nonzero signed-flow entries.  Moreover the exact
   element-incidence invariant degrades by a factor \(\Theta(m)\) under flow
   error.  Hence an \(o(W)\), rather than \(o(W/m)\), defect tolerance
   is too coarse for orbit arithmetic to force a contradiction.

The proved boundary is therefore precise: on every even \(m\), exact
integral \(BA\)-flow is incompatible with any nonempty owner-disjoint
packing; on the odd-prime subsequence, exact flow together with exact
owner coverage is arithmetically impossible.  Neither statement decides
the requested \(o(W)\)-leave, \(o(W)\)-defect rounding.  Its live content
is a critical-scale \(\Theta(W/m)\) atom-packing problem.

## 1. The atom packing and its owner windows

For a permutation state

\[
                  \pi=(x_1,\ldots,x_n),
\]

put

\[
 X(\pi)=\{x_1,\ldots,x_m\},\qquad
 Y(\pi)=X(A\pi)=\{x_2,\ldots,x_{m+1}\}.
\tag{1.1}
\]

Every selected nested-star atom has three source states.  Its six
owners are the three \(X(\pi)\)'s and three \(Y(\pi)\)'s.  An
owner-disjoint atom packing therefore has

\[
 |S|=3a={W-\ell\over2},
\tag{1.2}
\]

and all \(2|S|\) sets in

\[
                  \{X(\pi),Y(\pi):\pi\in S\}
\tag{1.3}
\]

are distinct.

The permutation \(C=BA\) acts by

\[
 C(x_1,\ldots,x_n)
 =(x_3,x_4,\ldots,x_{n-1},x_1,x_n,x_2).
\tag{1.4}
\]

Let σ be the induced new-position-to-old-position permutation, so
that

\[
                  (C\pi)_i=\pi_{\sigma(i)}.
\]

Its two position cycles are

\[
 \mathcal O=(1,3,5,\ldots,2m-1),
 \qquad
 \mathcal Q=(2,4,\ldots,2m,2m+1),
\tag{1.5}
\]

of lengths \(m\) and \(m+1\), respectively.  Thus every \(C\)-orbit
of states has length \(L=m(m+1)\).

## 2. The even-\(m\) owner collision

Let

\[
                  P_0=\{1,\ldots,m\},\qquad
                  P_1=\{2,\ldots,m+1\}.
\tag{2.1}
\]

Then \(X(\pi)=\pi(P_0)\), \(Y(\pi)=\pi(P_1)\), and

\[
                  X(C^j\pi)=\pi(\sigma^jP_0).
\tag{2.2}
\]

### Theorem 2.1 (exact shifted-window identity)

If \(m\) is even, then

\[
                  \boxed{\sigma^{m+1}P_0=P_1.}
\tag{2.3}
\]

Consequently \(X(C^{m+1}\pi)=Y(\pi)\) for every state \(\pi\).

#### Proof

Write \(m=2r\).  On the \(m\)-cycle \(\mathcal O\) in (1.5), exponent
\(m+1\) is congruent to \(1\pmod m\).  It therefore sends

\[
 P_0\cap\mathcal O=\{1,3,\ldots,m-1\}
\]

to

\[
                  \{3,5,\ldots,m+1\}=P_1\cap\mathcal O.
\]

On the \((m+1)\)-cycle \(\mathcal Q\) in (1.5), the same exponent is zero.
It fixes

\[
 P_0\cap\mathcal Q=\{2,4,\ldots,m\}
                 =P_1\cap\mathcal Q.
\]

The two parts give (2.3), and (2.2) gives the owner identity. □

### Corollary 2.2 (exact flow is impossible for even \(m\))

For an owner-disjoint atom packing with even \(m\),

\[
                         S\cap C^{m+1}S=\varnothing.
\tag{2.4}
\]

Hence \(S=C(S)\) implies \(S=\varnothing\).

#### Proof

If both \(\pi\) and \(C^{m+1}\pi\) belonged to \(S\), then the successor
owner \(Y(\pi)\) and the source owner \(X(C^{m+1}\pi)\) would coincide,
contrary to (1.3).  This proves (2.4).  A \(C\)-invariant nonempty set
contains \(C^{m+1}\pi\) with every \(\pi\) it contains, so it violates
(2.4). □

This is not a mere divisibility failure: for even \(m\), no nonempty
integral point exists on the exact \(BA\)-flow face, regardless of the
number of owners one is willing to leave.

### Theorem 2.3 (sharp robust collision bound)

If \(m\) is even, every owner-disjoint atom packing satisfies (0.4).

#### Proof

For any permutation \(C\) and any indicator \(y\), telescoping and
invariance of the \(\ell^1\)-norm give

\[
 \lVert y-y\circ C^{-(m+1)}\rVert _1
 \le (m+1)\lVert y-y\circ C^{-1}\rVert _1.
\tag{2.5}
\]

Take \(y={\bf1}_S\).  By (2.4), the two sets \(S\) and
\(C^{m+1}S\) are disjoint, so the left side of (2.5) is \(2|S|\).
Use (1.2) and (0.1). □

The inequality is sharp for the collision mechanism itself.  On one
\(C\)-orbit, index states as \(v_j=C^jv_0\), \(j\in\mathbb Z/L\mathbb
Z\), and write uniquely

\[
                  j=a+(m+1)b,\qquad
                  0\le a\le m,\quad0\le b<m.
\]

Let

\[
                  S_* =\{v_{a+(m+1)b}:b\text{ is even}\}.
\tag{2.6}
\]

Then \(|S_*|=L/2\), \(S_*\cap C^{m+1}S_*=\varnothing\), and a
one-step \(C\)-boundary occurs only when \(a\) wraps from \(m\) to
zero.  Therefore

\[
 \lVert d_{S_*}\rVert _1=m={2|S_*|\over m+1}.
\tag{2.7}
\]

In fact all \(L\) owners \(X(\pi),Y(\pi)\), \(\pi\in S_*\), are
distinct.  Indeed \(P_0\) and \(P_1\) have trivial stabilizer under
\(\sigma\), and the unique solution of
\(\sigma^jP_0=\sigma^kP_1\) is
\(j-k\equiv m+1\pmod L\).  The choice (2.6) excludes exactly those
pairs.  Thus (2.7) is sharp even after imposing all owner inequalities
inside one orbit.  It does not assert that \(S_*\) partitions into
nested-star triples; Lemma 4.3 of the owner-nibble report shows that
the three sources of one atom must lie in three different \(BA\)-orbits.

For odd \(m\), no within-orbit source/successor collision exists:
\(P_0\) contains \((m+1)/2\) positions of \(\mathcal O\), whereas \(P_1\) contains
\((m-1)/2\).  Since powers of \(\sigma\) preserve \(\mathcal O\), no power can send
\(P_0\) to \(P_1\).

## 3. Exact-flow element arithmetic

Every \(C\)-orbit \(\mathscr O\) has a canonical label bipartition

\[
 P_{\mathscr O}=\{\text{labels occupying positions in }\mathcal O\},
 \qquad |P_{\mathscr O}|=m,
\tag{3.1}
\]

with complementary \((m+1)\)-set \(Q_{\mathscr O}\).  It is invariant
along the orbit.

For a label \(c\), define its paired owner-incidence at a state by

\[
 h_c(\pi)={\bf1}_{\{c\in X(\pi)\}}
          +{\bf1}_{\{c\in Y(\pi)\}}.
\tag{3.2}
\]

### Lemma 3.1 (full-orbit incidence)

On a full \(C\)-orbit \(\mathscr O\),

\[
 \sum_{\pi\in\mathscr O}h_c(\pi)
 =
 \begin{cases}
       L,&c\in P_{\mathscr O},\\
       m^2,&c\in Q_{\mathscr O}.
 \end{cases}
\tag{3.3}
\]

#### Proof

As \(\pi\) traverses a full orbit, a label in \(P_{\mathscr O}\) visits
each position of \(\mathcal O\) exactly \(m+1\) times.  The total multiplicity of
the odd positions in the two windows \(P_0,P_1\) is

\[
 |P_0\cap\mathcal O|+|P_1\cap\mathcal O|=m.
\]

Its incidence is therefore \(m(m+1)=L\).  A label in
\(Q_{\mathscr O}\) visits each position of \(\mathcal Q\) exactly \(m\) times,
and the corresponding two-window multiplicity is again \(m\).  Its
incidence is \(m^2\). □

Suppose now that \(d_S=0\).  Then \(S\) is a union of \(T\) full
\(C\)-orbits.  Let

\[
 t_c=|\{\mathscr O\subset S:c\in P_{\mathscr O}\}|.
\tag{3.4}
\]

Let ℒ be the unused-owner family and

\[
 \ell_c=|\{X\in\mathscr L:c\in X\}|.
\tag{3.5}
\]

Every label belongs to

\[
 N=\binom{2m}{m-1}=m\operatorname {Cat}_m
\tag{3.6}
\]

middle owners.

### Theorem 3.2 (exact orbit-owner equations)

Every exact-flow owner-disjoint packing satisfies

\[
 \boxed{
   LT={W-\ell\over2},\qquad
   N-\ell_c=m^2T+mt_c\quad(c\in[n]).}
\tag{3.7}
\]

Consequently

\[
 \boxed{\ell\equiv W\pmod {2L},\qquad
        \ell_c\equiv0\pmod m\quad(c\in[n]).}
\tag{3.8}
\]

If ℒ is nonempty, then necessarily

\[
                              \ell\ge m+1.
\tag{3.9}
\]

#### Proof

The first equation is (1.2) and \(|S|=LT\).  The second follows by
summing (3.3) over the selected orbits:

\[
 N-\ell_c=L t_c+m^2(T-t_c)=m^2T+mt_c.
\]

This gives (3.8).  For (3.9), pick one leave edge \(X\in\mathscr L\).
Every \(c\in X\) has positive degree \(\ell_c\) and hence degree at least
\(m\) by (3.8).  If \(\ell\le m\), all \(m\) vertices of \(X\) must lie
in every leave edge.  Since every leave edge has size \(m\), all leave
edges would equal \(X\), contradicting simplicity unless there were
only one edge; one edge has degree one and also contradicts (3.8).
Thus \(\ell\ge m+1\).  The abstract bound is sharp: the \(m+1\) many
\(m\)-subsets of a fixed \((m+1)\)-set all have degree \(m\). □

### Corollary 3.3 (exact-cover divisibility)

If an exact-flow packing covers every owner, then

\[
 T={n\operatorname {Cat}_m\over2m(m+1)},
 \qquad
 t_c={\operatorname {Cat}_m\over2(m+1)}\quad(c\in[n]),
\tag{3.10}
\]

and hence

\[
                         2m(m+1)\mid\operatorname {Cat}_m.
\tag{3.11}
\]

For every prime \(m=p>2\), (3.11) fails.

#### Proof

Set \(\ell=\ell_c=0\) in (3.7), use \(W=n\operatorname {Cat}_m\), and
solve.  Since \(T=nt_c/m\) and \(\gcd(n,m)=1\), integrality of \(T,t_c\)
forces \(m\mid t_c\), which is (3.11).

For prime \(p\), the coefficient of \(x^p\) in

\[
 (1+x)^{2p}\equiv(1+x^p)^2\pmod p
\]

gives \(\binom{2p}{p}\equiv2\pmod p\).  Since \(p+1\equiv1\pmod p\),

\[
 \operatorname {Cat}_p={1\over p+1}\binom{2p}{p}\equiv2\pmod p.
\]

Thus \(p\nmid\operatorname {Cat}_p\). □

The total atom count also gives the elementary congruence

\[
                         \ell\equiv W\pmod6.
\tag{3.12}
\]

Equations (3.8), (3.11), and (3.12) are exact arithmetic conditions,
but their moduli are only polynomial in \(m\).  They cannot by
themselves force a leave comparable with \(W\).

## 4. Why approximate flow destroys the congruences

Fix a \(C\)-orbit and label it \(v_j=C^jv_0\), \(j\in\mathbb Z/L\mathbb
Z\).  Put \(y_j={\bf1}_S(v_j)\) and \(d_j=y_j-y_{j-1}\).

### Lemma 4.1 (Smith form and the orbit moment)

The integer matrix \(I-C\) on one \(L\)-cycle has Smith normal form

\[
                     \operatorname {diag}(1,\ldots,1,0).
\tag{4.1}
\]

Its integer image is exactly the lattice of vectors whose coordinate
sum is zero.  Moreover

\[
                 |S\cap\mathscr O|+\sum_{j=0}^{L-1}j\,d_j
                 \equiv0\pmod L.
\tag{4.2}
\]

#### Proof

The matrix is the signed incidence matrix of a directed cycle.  Delete
one row and one column; the remaining directed-path incidence minor
has determinant \(\pm1\).  The rank is \(L-1\), proving (4.1) and the image
claim.

For (4.2), calculate modulo \(L\):

\[
 \sum_jj d_j
 =\sum_jj y_j-\sum_jj y_{j-1}
 \equiv\sum_jj y_j-\sum_j(j+1)y_j
 =-\sum_jy_j.
\]

This is (4.2). □

There is therefore no hidden mod-\(p\) torsion in the \(BA\)-flow
rows.  The only linear invariant on an orbit is zero total divergence.
Indeed, for every \(1\le r<L\), the interval

\[
                         \{v_0,\ldots,v_{r-1}\}
\]

has cardinality \(r\), while its defect has only the two nonzero
entries \(d_0=1,d_r=-1\).  Thus every residue modulo \(L\) is changed
at \(\ell^1\)-cost two.  Exact orbit-length divisibility is not robust
under even an \(O(1)\) signed-flow allowance.

There is also a useful exact stability identity for the element
equations.  Let

\[
 p_c(\pi)={\bf1}_{\{c\text{ lies in the }\mathcal O
                         \text{-position label class of }\pi\}}.
\tag{4.3}
\]

This is constant on \(C\)-orbits.  The orbit mean in Lemma 3.1 is

\[
 \mu_c(\pi)={m\over m+1}+{p_c(\pi)\over m+1}.
\tag{4.4}
\]

### Theorem 4.2 (approximate element-incidence identity)

For every owner-disjoint atom packing and every label \(c\),

\[
 N-\ell_c
 ={m\over m+1}|S|+{1\over m+1}\sum_{\pi\in S}p_c(\pi)+E_c,
\tag{4.5}
\]

where

\[
                         |E_c|\le(m+1)\Delta_{BA}(S).
\tag{4.6}
\]

#### Proof

On each \(C\)-orbit, the function \(h_c-\mu_c\) has mean zero.  It has
period \(m\) when \(p_c=1\), and period \(m+1\) when \(p_c=0\).  Hence
there is a periodic function \(g_c\) such that

\[
                         h_c-\mu_c=g_c-g_c\circ C,
\tag{4.7}
\]

and one may choose

\[
                         \operatorname {osc}(g_c)\le m+1.
\tag{4.8}
\]

To see (4.8), define \(g_c\) by successive partial sums over one short
period.  The range of those partial sums is at most the total positive
mass of \(h_c-\mu_c\), which is at most \(m+1\).

Summing (4.7) over \(S\) gives

\[
 \sum_{\pi\in S}(h_c(\pi)-\mu_c(\pi))
 =\sum_\pi g_c(\pi)d_S(\pi).
\]

The defect has sum zero on each orbit.  Subtract the midpoint of the
range of \(g_c\) separately on each orbit, and use (4.8):

\[
 \left|\sum_\pi g_c(\pi)d_S(\pi)\right|
 \le {m+1\over2}\lVert d_S\rVert _1
 =(m+1)\Delta_{BA}(S).
\]

Finally \(\sum_{\pi\in S}h_c(\pi)=N-\ell_c\) by owner-disjointness, and summing (4.4)
gives (4.5). □

The factor \(m\) in (4.6) is of the correct order: along the
\(m\)-position cycle, \(h_c-1\) consists of a positive block and a
negative block, each of length \(\Theta(m)\), so every primitive in (4.7)
has oscillation \(\Theta(m)\).  Therefore (4.5) yields a useful \(o(W)\)
element-balance conclusion only under

\[
                         \Delta_{BA}=o(W/m),
\tag{4.9}
\]

not under the requested weaker hypothesis \(\Delta_{BA}=o(W)\).

## 5. The parity character

The coordinate permutation \(C\) has sign

\[
 (-1)^{m-1}(-1)^m=-1.
\]

Thus, with \(\varepsilon(\pi)\) the sign of a permutation state,

\[
                         \varepsilon(C\pi)=-\varepsilon(\pi).
\]

Consequently

\[
 \boxed{
 2\sum_{\pi\in S}\varepsilon(\pi)
 =\sum_\pi\varepsilon(\pi)d_S(\pi),\qquad
 \left|\sum_{\pi\in S}\varepsilon(\pi)\right|
 \le\Delta_{BA}(S).}
\tag{5.1}
\]

This parity relation supplies no atom-count obstruction.  For \(m\ge3\),
fixing a canonical atom and its six owners still leaves \(m-1\ge2\)
nonfinal entries in each ordered \(P\)-block.  Transposing two of those
entries flips the sign of that source state without changing any owner,
endpoint, common suffix, or either of the other two source states.
Hence the signs of the three source states can be toggled independently
within the labelled atom catalogue.

## 6. Exact proved boundary

The invariant audit yields a genuine obstruction and an equally
important limitation.

* For even \(m\), exact \(BA\)-flow and a nonempty owner-disjoint atom
  packing are incompatible, for the structural reason (0.2).
* Any near-cover on even \(m\) must incur signed defect at least
  \(\Theta(W/m)\); this lower bound is locally sharp.
* For odd \(m\), exact flow still faces the divisibility and balanced
  orbit-label equations (3.7); exact owner coverage is excluded for
  every odd prime.
* All flow-lattice mod-\(p\) and parity obstructions can be absorbed at
  \(o(W)\) signed cost.  The exact arithmetic does not exclude an
  owner leave \(o(W)\) together with signed divergence \(o(W)\).

Thus the next constructive statement cannot be an exact-flow rounding
theorem.  It must be a nested-star atom packing whose \(BA\)-boundary is
at the critical order \(O(W/m)\) (or, at minimum, \(o(W)\)), while
covering \(W-o(W)\) owners.  The alternating half-orbit block (2.6)
identifies the correct even-\(m\) phase pattern, but the unresolved
step is to synchronize such phases across triples of distinct
\(BA\)-orbits so that every triple is a legal nested-star atom.
