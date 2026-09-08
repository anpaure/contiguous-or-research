# Strict-spiral lifetime existence and the dense shadow gate

Date: 2026-07-29

Status: unconditional arithmetic existence theorem, unconditional
middle/`q1` existence theorem via the MMM projection, exact quantitative
obstructions to combining them sparsely, and a reconciliation of the
audited `k=7,9,11,15` schedules.  No all-`k` decorated carrier or new
`k=15` word is claimed.

Primary inputs:

* `MATH_THEOREM_STRICT_SPIRAL_EVENT_STREAM_LIFETIME_AND_DUAL_RESIDENCE_20260729.md`;
* `MATH_DESIGN_K15_ALPHA_BETA_LIFETIME_BENDERS_20260729.md`;
* `MATH_MERINO_MICKA_MUTZE_STRICT_SPIRAL_PROJECTION_20260729.md`;
* `MATH_ATLAS_STRICT_SPIRAL_RUNTRACE_SOLUTIONS_20260729.md`.

## 0. Verdict

The lifetime/gap feasibility problem is completely soluble by an explicit
cycle-joining construction.  For every odd

\[
 m\ge1,\qquad k=2m+1,\qquad r=m+1,\qquad
 N=\operatorname{Cat}_m,\qquad W=kN,
\]

there is an exact run-transversal schedule with all zero gaps equal to
\(m\) and all positive lifetimes in

\[
 \{m,m+1,m+2\}.
\]

It is simultaneously non-lazy through lower and upper depth \(m-1\).
This is essentially the strongest possible two-sided residence statement.

It does **not** solve the carrier problem.  The construction changes only
\(O(k)\) blocks from a period-\(k\) word.  Middle injectivity forces at
least \(N\) physical period-\(k\) defects, so the construction is
rigorously non-Hamilton at \(k=15\), and asymptotically throughout the
Catalan regime.

Separately, the Merino--Mička--Mütze projection gives, for every odd \(k\),
an exact lifetime/gap schedule whose middle and lower-`q1` decks are
bijective.  Its residence and deeper shadows need not be good.  Thus the
two existence statements are individually closed, while their simultaneous
refinement is the genuine open theorem.

The solved `k=7,9,11` schedules show that dual residence is not the missing
refinement: every one has minimum zero gap one, yet all required upper
targets occur.  Any successful induction must transport the insertion-prefix
support ledger, not insist that every nominal-width upper window have the
expected rank.

## 1. Exact schedule notation

Unwrap one scalar trace over \([0,W]\).  Let its \(N\) positive runs occur
in physical cyclic order, with start seams

\[
 0=p_0<p_1<\cdots<p_N=W,
\]

positive lifetimes \(\ell_t\), and following zero gaps \(g_t\):

\[
 p_{t+1}=p_t+\ell_t+g_t.                             \tag{1.1}
\]

The scalar word is one on \((p_t,p_t+\ell_t]\) and zero on the following
gap.  Put

\[
 s_t=p_t\pmod N,\qquad e_t=p_t+\ell_t\pmod N.      \tag{1.2}
\]

The event-stream normal form says that this is a rank-\(r\), unit-voltage
strict Johnson schedule exactly when

\[
 (s_t)_t\text{ and }(e_t)_t\text{ are permutations of }\mathbb Z_N,
                                                                  \tag{1.3}
\]

\[
 \ell_t,g_t>0,\qquad
 \sum_t\ell_t=rN,\qquad \sum_tg_t=mN.             \tag{1.4}
\]

The carrier is then

\[
 T_i=\{x\in\mathbb Z_k:c_{i-xN}=1\}.                \tag{1.5}
\]

Minimum lifetime \(d+1\) gives a non-lazy lower erosion tower through
depth \(d\); minimum gap \(u+1\) gives the analogous upper tower through
depth \(u\).  Neither assertion includes target coverage.

## 2. Constant gaps are winding Hamilton residue cycles

The first reduction removes half of the composition variables.

### Theorem 2.1 (constant-gap equivalence)

Fix every zero gap to be \(m\).  Exact schedules (1.1)--(1.4) are in
bijection with the following data:

1. a directed Hamilton cycle \(P\) on \(\mathbb Z_N\); and
2. positive integer edge lifts \(h_x\), one at every \(x\in\mathbb Z_N\),
   satisfying

   \[
    h_x\equiv P(x)-x\pmod N,\qquad
    \sum_xh_x=kN,\qquad h_x\ge m+1.               \tag{2.1}
   \]

The lifetime at start residue \(x\) is

\[
 \boxed{\ell_x=h_x-m.}                              \tag{2.2}
\]

The schedule is lower-resident through depth \(d\) exactly when

\[
 \min_xh_x\ge m+d+1,                                \tag{2.3}
\]

and it is automatically upper-resident through every depth
\(u\le m-1\).

#### Proof

Traverse the residue cycle \(P\), using physical increment \(h_x\) on the
edge leaving \(x\).  Congruence in (2.1) makes the successive start residues
exactly the vertices of \(P\), hence a permutation.  With (2.2), the end
residue of the run beginning at \(x\) is

\[
 x+\ell_x\equiv P(x)-m\pmod N.                      \tag{2.4}
\]

Since \(P\) is a permutation, the end residues are also a permutation.
Moreover

\[
 \sum_x\ell_x=\sum_xh_x-mN=(k-m)N=(m+1)N=rN,
\]

and the constant gaps sum to \(mN\).  This proves sufficiency.

Conversely, in a constant-gap schedule, the physical start order induces
one directed Hamilton cycle \(P\) on the start residues.  Its physical
increments are \(h_x=\ell_x+m\), which satisfy (2.1), and (2.4) shows that
end transversality is automatic.  The residence assertions are exactly
\(\ell_x\ge d+1\) and \(m\ge u+1\).  \(\square\)

Thus the arithmetic part of the lifetime master is a winding-\(k\)
Hamilton-cycle problem on \(\mathbb Z_N\).  The shadow problem asks for a
very special such cycle, not merely any Hamilton cycle.

## 3. Explicit paired-successor construction

Put

\[
 g=\gcd(k,N),\qquad M=N/g.                         \tag{3.1}
\]

The translation

\[
 f_0(x)=x+k\pmod N                                  \tag{3.2}
\]

has exactly \(g\) directed cycles, the residue classes modulo \(g\).

For the Catalan values here, if \(g>1\), then \(M\ge2\).  Indeed, for
\(m\le4\), direct values \(N=1,2,5,14\) give \(g=1\); for \(m\ge5\),
\(N>k\ge g\).  The latter follows from \(C_5=42>11\) and the elementary
Catalan ratio \(C_{m+1}/C_m=2(2m+1)/(m+2)\).

### Lemma 3.1 (disjoint adjacent splice sources)

Assume \(g>1\).  For \(0\le c\le g-2\), put

\[
 q_c=c\pmod2,\qquad
 a_c=c+q_cg,\qquad b_c=a_c+1.                     \tag{3.3}
\]

The \(2(g-1)\) sources \(a_c,b_c\) are distinct elements of
\(\mathbb Z_N\).  The pair \((a_c,b_c)\) lies in the two adjacent
\(f_0\)-cycles \(c,c+1\) modulo \(g\).

#### Proof

Because \(M\ge2\), one has \(N\ge2g\), so every integer in (3.3) lies in
\([0,N-1]\).  Sources having nonadjacent residues modulo \(g\) cannot
coincide.  The only possible collision is
\(b_{c-1}=a_c\); the two use different values of \(q\) because the parity
alternates, so they differ by \(g\).  \(\square\)

### Theorem 3.2 (paired-successor lifetime construction)

For each \(c=0,\ldots,g-2\), replace the two standard successors

\[
 a_c\longmapsto a_c+k,\qquad
 b_c\longmapsto b_c+k
\]

by

\[
 a_c\longmapsto b_c+k,\qquad
 b_c\longmapsto a_c+k.                              \tag{3.4}
\]

The resulting successor permutation \(P\) is one Hamilton cycle on
\(\mathbb Z_N\).  Give its edges the physical lifts

\[
 h_{a_c}=k+1,\qquad h_{b_c}=k-1,\qquad h_x=k
 \quad\text{otherwise}.                             \tag{3.5}
\]

Then Theorem 2.1 gives the exact schedule

\[
 \ell_{a_c}=r+1,\qquad
 \ell_{b_c}=r-1,\qquad
 \ell_x=r\quad\text{otherwise},                    \tag{3.6}
\]

\[
 \boxed{g_x=m\quad\text{for every }x.}             \tag{3.7}
\]

Consequently both start and end residues are permutations, the sums are
exact, and:

* if \(g=1\), the constant schedule \(\ell\equiv r,g\equiv m\) is
  biresident through \((m,m-1)\);
* if \(g>1\), (3.6)--(3.7) is biresident through \((m-1,m-1)\).

#### Proof

Swapping the successors of vertices in two distinct directed cycles merges
those cycles into one.  Apply the switches in increasing \(c\).  After the
first \(c\) switches, the original classes \(0,1,\ldots,c\) form one
cycle, while class \(c+1\) is untouched.  Lemma 3.1 ensures that the next
two standard successor edges have not previously changed, so (3.4) merges
the next class.  Induction gives one Hamilton cycle.

The new physical differences are exactly \(k+1\) and \(k-1\); all other
edges retain difference \(k\).  Each pair preserves their sum, so
\(\sum_xh_x=kN\).  Theorem 2.1 gives (3.6)--(3.7).  Equivalently, the
endpoint calculation is literal:

\[
 a_c+(r+1)=b_c+r,\qquad
 b_c+(r-1)=a_c+r.                                   \tag{3.8}
\]

Thus each switch merely exchanges two images of the baseline endpoint
permutation \(x\mapsto x+r\).  The minimum lifetime is \(r\) when
\(g=1\), and \(r-1=m\) otherwise; every gap is \(m\).  This proves all
claims.  \(\square\)

For general voltage \(v\), the quotient event streams are recovered without
choices.  If a run starts at \(p=j+Ns\) and ends at \(e=h+Nq\), then

\[
 \beta_j=-sv\pmod k,\qquad \alpha_h=-qv\pmod k.  \tag{3.9}
\]

### Corollary 3.3 (the explicit `k=15` schedule)

At \(k=15\),

\[
 m=7,\quad r=8,\quad N=429,\quad g=3.
\]

The construction has lifetime histogram

\[
 \boxed{7^2,8^{425},9^2}                          \tag{3.10}
\]

and gap histogram \(7^{429}\).  It is simultaneously non-lazy through
lower and upper depth six.  This proves that the current `k=15` difficulty
is not arithmetic feasibility or two-sided residence.

## 4. Arithmetic sharpness and the sparse-splice obstruction

### Theorem 4.1 (sharp maximal biresidence)

A schedule biresident through \((m,m-1)\) exists if and only if

\[
 \gcd(k,N)=1.                                       \tag{4.1}
\]

#### Proof

Lower depth \(m\) requires \(\ell_t\ge m+1=r\) for every \(t\).  Since
their average is exactly \(r\), all lifetimes equal \(r\).  Upper depth
\(m-1\) requires \(g_t\ge m\); their average is \(m\), so all gaps equal
\(m\).  Every physical start increment is therefore \(k\), and the start
residues form one cycle precisely when translation by \(k\) is transitive on
\(\mathbb Z_N\), i.e. precisely when (4.1) holds.  The constant schedule
proves sufficiency.  \(\square\)

This theorem is only about the lifetime normal form.  Even in the coprime
case the resulting trace is period \(k\), so it is not a middle Hamilton
cycle when \(N>1\).

The next lemma quantifies that failure.

### Lemma 4.2 (every Hamilton trace has linearly many shift defects)

For a cyclic scalar trace \(c\) and \(t\in\mathbb Z_W\), put

\[
 D_t(c)=\{p\in\mathbb Z_W:c_{p+t}\ne c_p\}.         \tag{4.2}
\]

If the physical middle states (1.5) are all distinct, then for every
nonzero \(t\in\mathbb Z_W\),

\[
 \boxed{|D_t(c)|\ge N.}                             \tag{4.3}
\]

#### Proof

If \(|D_t|<N\), then

\[
 \left|\bigcup_{x\in\mathbb Z_k}(D_t+xN)\right|
 \le k|D_t|<kN=W.
\]

Choose \(i\) outside this union.  Then
\(i-xN\notin D_t\) for every coordinate \(x\), so

\[
 c_{i+t-xN}=c_{i-xN}\qquad(x\in\mathbb Z_k).
\]

Equation (1.5) gives \(T_{i+t}=T_i\), contradicting physical
Hamiltonicity.  \(\square\)

### Theorem 4.3 (the paired-successor construction is too sparse)

In Theorem 3.2, let

\[
 A=2(g-1)
\]

be the number of anomalous blocks.  Then

\[
 \boxed{|D_k(c)|\le 2A(k+1)=4(g-1)(k+1).}           \tag{4.4}
\]

Therefore, when \(N>1\), the construction is not middle Hamilton whenever

\[
 N>4(g-1)(k+1).                                     \tag{4.5}
\]

At \(k=15\), (4.4) is at most \(128<429=N\), so the explicit schedule is
rigorously non-Hamilton.

#### Proof

Partition the scalar trace into the blocks beginning at successive run
starts.  A normal block is \(1^r0^m\) and has length \(k\).  The \(A\)
anomalous blocks are \(1^{r+1}0^m\) or \(1^{r-1}0^m\), of length
\(k+1\) or \(k-1\).  If a block and its successor are both normal, shifting
the first block by \(k\) matches it pointwise with the successor.  Thus
\(D_k(c)\) is contained in the union of every anomalous block and every
immediate predecessor block.  There are at most \(2A\) such blocks, each of
length at most \(k+1\), proving (4.4).  Lemma 4.2 proves (4.5).  \(\square\)

The conclusion is structural: a successful construction must introduce
\(\Omega(N)\) physical shift defects.  Joining the \(g\) arithmetic cycles
with only \(O(g)\) local splices can never supply the necessary necklace
entropy once \(N\) is Catalan-large.

## 5. Middle and `q1` injectivity nevertheless exist for every odd `k`

The arithmetic construction above should not be mistaken for a no-go on the
normal form itself.

### Theorem 5.1 (MMM lifetime schedule)

For every odd \(k=2m+1\) and every unit voltage \(v\in\mathbb Z_k^\times\),
there exists an exact lifetime/gap schedule satisfying (1.1)--(1.4) such
that:

1. the \(N\) middle quotient states represent all central rotation orbits;
2. the \(N\) adjacent intersections represent all lower-central rotation
   orbits; and
3. the physical lift is one Hamilton Johnson cycle of voltage \(v\).

#### Proof

The rotational Middle Levels theorem of Merino--Mička--Mütze projects to a
strict-spiral Johnson Hamilton cycle with a perfect lower-`q1` deck and
prescribed unit voltage.  Apply the exact event-stream lifetime theorem to
its scalar trace.  Its run starts and ends give the two permutations in
(1.3), and its rank gives (1.4).  The two asserted decks are exactly the
upper and lower shores of the projected Middle Levels Hamilton cycle.
\(\square\)

This theorem closes lifetime feasibility **together with** middle/`q1`
injectivity.  It supplies only the automatic minimum lifetime two; it does
not prove the compiler residence depth or deeper lower/upper coverage.

Theorems 3.2 and 5.1 therefore solve two different projections of the
desired construction:

\[
\begin{array}{c|c|c}
 &\text{deep two-sided residence}&\text{middle/`q1` decks}\\ \hline
\text{paired-successor schedule}&\checkmark&\times\\
\text{MMM schedule}&\text{not guaranteed}&\checkmark
\end{array}
\]

No theorem currently intersects the two rows for general \(k\).

## 6. Exact lifetime-to-shadow criterion

For a schedule \((p,\ell,g)\), define the fibre word

\[
 A_j(x)=c_{j-xN},\qquad x\in\mathbb Z_k.            \tag{6.1}
\]

Thus \(A_j=T_j\).  Put

\[
 L_j=A_j\cap A_{j+1},\qquad
 Q_j^{(q)}=\bigcap_{a=0}^{q}A_{j+a}\quad(q\ge2),
 \qquad Q_j=Q_j^{(2)},                              \tag{6.2}
\]

and, for width \(w\ge1\),

\[
 V_{j,w}=\bigcup_{a=0}^{w-1}A_{j+a}.                \tag{6.3}
\]

### Theorem 6.1 (complete orbit criterion)

The schedule is middle and lower-`q1` perfect exactly when the \(N\)
rotation necklaces

\[
 [A_j],\qquad [L_j]\qquad(0\le j<N)              \tag{6.4}
\]

are separately pairwise distinct.  It has complete lower-`q2` support
exactly when every actual rotation orbit of rank \(r-2\) occurs among the
\([Q_j]\).  More generally, lower depth \(q\) is complete exactly when
every required rank-\(r-q\) orbit occurs among \([Q_j^{(q)}]\).  Its
arbitrary-width upper intervals cover every upper target exactly when every
actual upper rotation orbit occurs among

\[
 [V_{j,w}]\qquad(0\le j<N,\ 1\le w\le W).        \tag{6.5}
\]

At composite \(k\), “actual orbit” is essential: noncentral ranks can have
short orbits, and replacing (6.5) by a free-orbit count is invalid.

#### Proof

Equations (6.1)--(6.3) are the event-stream intersection/union identities.
The two central rotation actions are free because their ranks are coprime
to \(k\).  Hence \(N\) distinct central necklaces lift to all \(W\)
physical states, and conversely any quotient collision gives a physical
collision.  At other ranks, strict equivariance carries one occurrence
through its complete actual orbit, proving the two support equivalences.
\(\square\)

For an algebraic induction, attach square-zero variables \(y_\nu,z_\lambda\)
to middle and `q1` necklaces, and ordinary variables
\(u_{q,\eta},v_\theta\) to lower-depth and upper target orbits.  For a
declared set \(\mathcal R\) of required lower depths, the schedule monomial

\[
 \prod_{j=0}^{N-1}y_{[A_j]}z_{[L_j]}
 \prod_{q\in\mathcal R}\prod_{j=0}^{N-1}u_{q,[Q_j^{(q)}]}
 \prod_{j,w}v_{[V_{j,w}]}                          \tag{6.6}
\]

is nonzero in the square-zero factors exactly when both central decks are
injective; divisibility by every required \(u_{q,\eta},v_\theta\) is exactly
the lower/upper support conditions.  Factors outside the required target
ranks are simply omitted.  Taking \(\mathcal R=\{2,\ldots,d\}\) records the
whole lower compiler band, while \(\mathcal R=\{2\}\) records only the q2
gate.  Equation (6.6) is an exact transfer-matrix target for a recursive
construction.  It is not itself an existence proof.

## 7. The successive gates do not imply one another

### Proposition 7.1 (perfect lifetime arithmetic can have one necklace)

At \(k=7,N=5,r=4\), let

\[
 c=(1111000)^5.                                     \tag{7.1}
\]

Every lifetime is four and every gap is three.  Both start and end residues
are permutations modulo five, so (7.1) is an exact run-transversal schedule,
biresident through \((3,2)\).  It even satisfies the complement law

\[
 1-c_p=c_{p+17}c_{p+18}.                            \tag{7.2}
\]

Nevertheless

\[
 T_{i+1}=\rho^3T_i,                                 \tag{7.3}
\]

so all five quotient owners lie in one rotation necklace; the same is true
of the lower-`q1` row.

#### Proof

Run starts are seven apart, whose residues modulo five are a permutation;
end residues are their translate by four.  Since \(17\equiv3\pmod7\),
(7.2) is checked on the seven-symbol block.  Finally
\(5\cdot3\equiv1\pmod7\); substituting this into (1.5) gives (7.3).
\(\square\)

Thus positivity, the two endpoint permutations, maximal residence, and even
aligned complement pairing do not imply either central deck.

### Proposition 7.2 (the two central decks do not imply deeper support)

The audited resident `k=15` seed has:

* exact start/end residue permutations and lifetime/gap sums;
* minimum lifetime four;
* perfect middle and lower-`q1` decks;
* 47 missing lower-`q2` target orbits; and
* 95 missing arbitrary-width upper target orbits.

Therefore lifetime feasibility plus compiler residence plus both central
decks still does not imply the coupled deeper decoration.

These two propositions prove that the missing all-`k` theorem must control
the orbit monomial (6.6) directly.  No statistic involving only lifetime and
gap histograms can do so.

The reverse independence is now visible inside the complement-coherent
`k=15` face as well.  The audited mixed-step trace with SHA-256
`de3786f9b6b3f3b211e991fbf9f38a2f0a5026b6d63eee07810439c2746d3936`
has complete lower-`q2` support (hence complete dual
upper-`q1` support), correct rank/Johnson/residence data, but only 367 of the
429 middle necklaces.  Thus standalone `q2` feasibility does not supply the
central squarefree deck either.

## 8. Complement coherence is a special, not general, collapse

Assume \(W=2s+1\).  Complement coherence of the scalar trace is

\[
 1-c_p=c_{p+s}c_{p+s+1}.                            \tag{8.1}
\]

Let run \(t\) have start seam \(p_t\), end \(e_t=p_t+\ell_t\), and
following gap \(g_t=p_{t+1}-e_t\).  Then (8.1) is equivalent to an aligned
pairing \(\phi\) of gaps with runs satisfying

\[
 p_{\phi(t)}=e_t+s,\qquad
 e_{\phi(t)}=p_{t+1}+s+1                            \tag{8.2}
\]

cyclically.  In particular,

\[
 \boxed{\ell_{\phi(t)}=g_t+1.}                     \tag{8.3}
\]

Equality of the unordered multisets \(\{\ell_t\}=\{g_t+1\}\) is weaker
than (8.2) and is not sufficient.

Indeed, (8.1) says that a zero position shifted by \(s\) is exactly an
internal adjacent pair of ones.  A zero gap of length \(g_t\) therefore
maps, endpoint by endpoint, to the \(g_t\) internal edges of one run of
length \(g_t+1\), giving (8.2); the converse endpoint tiling recovers
(8.1).

On this aligned face one has exactly

\[
 L_{i+s}=\overline{A_i},\qquad
 Q_{i+s}=\overline{A_i\cup A_{i+1}}.                \tag{8.4}
\]

Hence

\[
 \text{middle perfect}\Longleftrightarrow\text{lower-`q1` perfect},
                                                                  \tag{8.5}
\]

\[
 \text{lower-`q2` complete}\Longleftrightarrow
 \text{upper-`q1` complete}.                        \tag{8.6}
\]

The all-depth version shifts upper depth \(q\) to lower depth \(q+1\).

This does not furnish the general induction requested here:

1. Lucas' theorem gives \(W\) odd exactly when \(m+1\) is a power of two,
   equivalently when \(k\) is a Mersenne number.
2. At \(k=9,11\), the solved strict carriers have even \(W\), so internal
   complement coherence is impossible.
3. At \(k=7\), the audited complement-coherent strict class has no Hamilton
   member; Proposition 7.1 is its extremal periodic obstruction.

Complement coherence can halve the `k=15` decoration gates, but it cannot
be the induction mechanism explaining the known `k=7,9,11` certificates.

## 9. Reconciliation of the exact small schedules

All facts in this section are frozen-certificate statements, not an
extrapolated recurrence.

| case | `(N,r,d)` | `min ell / min gap` | middle/`q1` | deeper lower | all upper | final status |
|---|---|---:|---|---|---|---|
| `k=7` | `(5,4,2)` | `3 / 1` | exact | `q2` complete | complete | shadow-complete carrier |
| `k=9` | `(14,5,2)` | `3 / 1` | exact | `q2` complete | complete | word length `128`, `511/511` |
| `k=11` | `(42,6,3)` | `4 / 1` | exact | `q2,q3` complete | complete | word length `465`, `2047/2047` |
| `k=15` seed | `(429,8,3)` | `4 / 1` | exact | `47` `q2` orbit holes | `95` orbit holes | not a solution |

The two exact `k=7` run/gap representatives have

\[
 (\ell;g)=(7,4,3,3,3;\ 2,3,4,1,5)                 \tag{9.1}
\]

and

\[
 (\ell;g)=(3,4,7,3,3;\ 3,2,5,1,4).                \tag{9.2}
\]

Both cover all 21 rank-two targets with load histogram
\(1^7 2^{14}\), and their arbitrary unions cover ranks five, six, and
seven.  They are the two physical-rotation classes among the 70 indexed
middle/`q1`-perfect traces in the tiny audit.  Separately,
`MATH_THEOREM_RUN_TRANSVERSAL_EROSION_AND_GRADED_HALL_SEPARATION_20260729.md`
reports two decorated `k=7` states with a one-core/Hall `28/28` compiler.
The frozen artifacts do not explicitly identify those decorated states with
the two displayed representatives (9.1)--(9.2), so no such identification
is asserted here.

For the primary `k=9` atlas certificate, the histograms are

\[
 \ell:3^6,4^3,6,7^2,8,12,\qquad
 g:1^2,2^5,3^3,4,7,8,16.                     \tag{9.3}
\]

For the primary `k=11` atlas certificate, they are

\[
 \ell:4^{13}5^{12}6^5 7^4 8^2 9,10^2 11,12,14, \tag{9.4}
\]

\[
 g:1^4 2^5 3^{10}4^4 5^6 6^2 7^2 8^4 10,12^2 14^2.\tag{9.5}
\]

There is a second exact compiler-ready `k=11` carrier, frozen as
`scratch/k11_current_hinted_resolve.word` and independently accepted by
`scratch/k11_current_hinted_resolve.audit.json`, with lifetime histogram

\[
 4^{11}5^{10}6^6 7^7 8^4 9^2 10,13.
\]

It must not be conflated with (9.4).  Both compile exactly, so no lifetime
histogram is forced.

Three rigorous lessons follow.

1. Every solved schedule attains the minimum legal positive lifetime
   \(d+1\); none is dual-resident even through depth one.
2. Fixed-width upper waits and wrong-rank occurrences coexist with complete
   upper support.  An induction must preserve first-arrival prefixes, not
   every nominal-width rank.
3. The solved lifetime and gap sequences are globally irregular.  This is
   consistent with Lemma 4.2: middle injectivity needs a linear number of
   physical shift defects, whereas the easy arithmetic construction has
   only \(O(k)\).

## 10. The exact remaining existence statement

The strongest honest general conjecture exposed by the preceding theorems
is the following.

> **Decorated lifetime schedule `DLS(k,d)`.**  There is a cyclic schedule
> satisfying (1.1)--(1.4), with \(\min\ell\ge d+1\), for which the two
> central necklace products in (6.6) are squarefree, every required lower
> orbit at every compiler depth \(2\le q\le d\) divides the corresponding
> support product, and every upper target orbit divides the arbitrary-prefix
> product.

`DLS(k,d)` is a conjecture for general odd \(k\).  It is verified by the
audited schedules at `k=7,9,11`; it is open at `k=15`.  Even `DLS` would
still precede the exact common-core/Hall compiler.

The minimum new constructive object is therefore one of the following,
with neither presently known:

1. a **dense winding-\(k\) residue Hamilton cycle** whose induced block
   trace satisfies the squarefree/divisibility monomial (6.6); or
2. an extensive alternating-circuit/absorber acting on an MMM schedule that
   preserves the two squarefree central decks while correcting residence
   and all missing support orbits.

Theorem 3.2 proves that no extra arithmetic obstruction is hiding in the
normal form.  Theorem 4.3 proves that a bounded number of residue-cycle
splices cannot be the missing construction.  Propositions 7.1--7.2 prove
that neither lifetime histograms nor central injectivity can substitute for
the dense orbit-support condition.

## 11. Audit boundary

The new unconditional claims were checked by three independent routes:

1. endpoint residues in (3.8) directly verify the paired-successor
   construction without reconstructing a carrier;
2. the period-defect argument (4.2)--(4.5) independently certifies its
   failure of middle Hamiltonicity at `k=15`; and
3. the frozen `k=7,9,11` arrays were re-read in physical run order, with the
   source-voltage and unit-voltage gauges kept distinct.

No new finite search, SAT solve, or long local process was run.  The new
theorems in Sections 2--8 are analytic; Section 9 explicitly imports the
already frozen small-certificate audits.
