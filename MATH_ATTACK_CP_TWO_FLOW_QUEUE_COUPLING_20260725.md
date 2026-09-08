# Direct attack on \(\mathrm{CP}_A\): exact two-flow queue coupling

Date: 2026-07-25

Pure mathematics only. No computation, search, solver, or probabilistic
rounding assertion is used.

## 0. Verdict

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad H=\lceil A\sqrt m\rceil .
\]

The balanced-flow theorem in
`ROTOR_MULTI_FRAME_PACKET_RESOLUTION_20260725.md`, Theorem 4.8, gives one
lower deletion flag and one upper addition flag at every middle owner, with
exact floor/ceiling balance at every controlled depth.  The two integral
flows can be coupled along a bridge-one path only under a rigid queue
recurrence.  The recurrence is derived exactly below.

If

\[
 \alpha(X)=(a_1,\ldots,a_H),\qquad
 \beta(X)=(b_1,\ldots,b_H),
\]

are the lower deletion and upper addition words at \(X\), then a
bridge-one arc to a distinct owner \(Y=X-a_1+y\) exists precisely when,
for some \(x\in X-\{a_1,\ldots,a_H\}\),

\[
 \boxed{\alpha(Y)=(a_2,\ldots,a_H,x)}                                      \tag{0.1}
\]

and

\[
 \boxed{\beta(Y)=(a_1,\tau_y\beta(X)),}                                    \tag{0.2}
\]

where \(\tau_y\) deletes \(y\) from the upper queue if \(y\) is present,
and otherwise deletes the last queue entry.  Thus the lower word is a FIFO
queue of future departures, while the upper word is a recency queue of past
departures which have not yet returned.

This gives three rigorous conclusions.

1. The two independent totally-unimodular flows of Theorem 4.8 do not yet
   solve the chronology problem.  Along an internal path arc they must obey
   all \(2H\) ordered equalities (0.1)--(0.2), not merely the separate
   lower and upper target marginals.
2. An \(H\)-resident Johnson cycle couples the two flows exactly: its lower
   flags are forward intersections and its upper flags are backward unions.
   The recursive pair-cube cycles are examples.  Their complete coordinate
   orbit gives an explicit fractional \(\mathrm{CP}_A\) solution of path
   weight \(W/R=o(W/H)\), where \(R=2\ell\) and \(H=o(\ell)\).
3. Promotion cannot be the main coupling mechanism.  If a covering prefix
   transversal has a bridge-one path cover with \(p\) paths and \(r\)
   genuine rotor arcs, then
   \[
      \boxed{p+r\ge N_H.}                                                    \tag{0.3}
   \]
   Hence \(p=o(W/H)\) forces
   \(r\ge(e^{-A^2}-o_A(1))W\).  Last-position promotion is useful for
   splicing, but a valid CP construction must change its upper frame on a
   positive density of steps.

The unresolved step is now an exact integral discrepancy rather than an
SCD or tag-\(H\) issue.  One must round the symmetric mixed-frame measure on
long coupled cycles to an exact partition of the middle owners while still
covering every lower and upper target.  Section 6 states both the unrestricted
ordered-Hall discrepancy and a concrete recursive-cycle integer program.
The LP for the latter is solved explicitly; its integral low-path solution
is not proved here.

## 1. Full flags and the exact bridge equations

At a middle owner \(X\in\binom{[n]}m\), write the successive lower
deletions and upper additions as

\[
 \alpha(X)=(a_1,\ldots,a_H),\qquad
 \beta(X)=(b_1,\ldots,b_H),                                                  \tag{1.1}
\]

where the \(a_i\) are distinct elements of \(X\), and the \(b_i\) are
distinct elements of \([n]-X\).  Put

\[
 A_X=\{a_1,\ldots,a_H\},\quad
 B_X=\{b_1,\ldots,b_H\},\quad
 L_X=X-A_X,\quad R_X=[n]-(X\cup B_X).                                       \tag{1.2}
\]

The associated useful state is

\[
 \omega_X=
 (L_X;a_H,a_{H-1},\ldots,a_1,b_1,\ldots,b_H;R_X).                           \tag{1.3}
\]

For \(y\in[n]-X\), define an ordered \((H-1)\)-word

\[
 \tau_y(b_1,\ldots,b_H)=
 \begin{cases}
  (b_1,\ldots,\widehat y,\ldots,b_H),&y\in B_X,\\
  (b_1,\ldots,b_{H-1}),&y\notin B_X.
 \end{cases}                                                               \tag{1.4}
\]

In the first line the hat means deletion at the unique position occupied by
\(y\).

### Theorem 1.1 (bridge-one in deletion/addition coordinates)

Let \(X\ne Y\) be middle owners carrying the full flags (1.1).  There is a
bridge-one arc \(\omega_X\to\omega_Y\) if and only if the following hold.

1. \(X,Y\) are Johnson adjacent and, writing
   \[
      X-Y=\{a\},\qquad Y-X=\{y\},                                           \tag{1.5}
   \]
   one has \(a=a_1\).
2. For some \(x\in L_X\),
   \[
      \alpha(Y)=(a_2,\ldots,a_H,x).                                         \tag{1.6}
   \]
3. The upper queue satisfies
   \[
      \beta(Y)=(a_1,\tau_y\beta(X)).                                        \tag{1.7}
   \]

If \(y\notin B_X\), the arc is a rotor shift.  If \(y=b_k\), it is the
singleton promotion at position \(H+k\).

#### Proof

In the notation (1.3), the bridge-one classification says that every arc
between distinct owners is either

\[
 (L;z_1,\ldots,z_{2H};R)
 \longmapsto
 (L-x+y;x,z_1,\ldots,z_{2H-1};R-y+z_{2H})                                  \tag{1.8}
\]

with \(x\in L,y\in R\), or

\[
 (L;z_1,\ldots,z_{2H};R)
 \longmapsto
 (L-x+z_{H+k};x,z_1,\ldots,\widehat{z_{H+k}},\ldots,z_{2H};R)               \tag{1.9}
\]

with \(x\in L\) and \(1\le k\le H\).  In both cases the source owner
loses \(z_H=a_1\).  Reversing the first \(H\) target singleton positions
gives

\[
 (a_2,\ldots,a_H,x),
\]

which is (1.6).  In (1.8), the last old upper singleton is discarded, so
the target upper word is

\[
 (a_1,b_1,\ldots,b_{H-1}).
\]

In (1.9), the arriving coordinate is \(b_k\) and is deleted from the old
upper word, giving

\[
 (a_1,b_1,\ldots,\widehat{b_k},\ldots,b_H).
\]

These are exactly (1.7).  Conversely, (1.5)--(1.7) reconstruct (1.8) or
(1.9), so the original bridge-one classification proves sufficiency.
\(\square\)

### Corollary 1.2 (the two forced first-band identities)

Every internal arc \(X\to Y\) of a bridge-one path satisfies

\[
 \boxed{\alpha_1(X)=X-Y=\beta_1(Y).}                                        \tag{1.10}
\]

Consequently

\[
 L_1(X)=X\cap Y,\qquad U_1(Y)=X\cup Y.                                     \tag{1.11}
\]

The first equality in (1.10) is (1.5), and the second is the first entry of
(1.7).  Equations (1.11) follow immediately.

## 2. Path normal form: future-deletion FIFO and past-deletion cache

Let

\[
 X_0\to X_1\to\cdots\to X_s                                                  \tag{2.1}
\]

be a bridge-one path through distinct owners.  For \(0\le t<s\), write

\[
 d_t\in X_t-X_{t+1},\qquad c_t\in X_{t+1}-X_t.                              \tag{2.2}
\]

Theorem 1.1 gives

\[
 d_t=\alpha_1(X_t),\qquad
 \alpha(X_{t+1})=(\alpha_2(X_t),\ldots,\alpha_H(X_t),x_t)                   \tag{2.3}
\]

for some \(x_t\in L_{X_t}\), and

\[
 \beta(X_{t+1})=(d_t,\tau_{c_t}\beta(X_t)).                                \tag{2.4}
\]

Thus, away from the right endpoint,

\[
 \alpha_i(X_t)=d_{t+i-1}                                                     \tag{2.5}
\]

whenever the indicated departure lies inside the path.  The lower flag is
therefore not free after the owner chronology is chosen: it is a sliding
window of the future departure word.

Equation (2.4) is an exact ordered-cache rule.  At step \(t\), prepend the
new departure \(d_t\).  If the arrival \(c_t\) is already in the cache,
remove that occurrence; otherwise evict the cache tail.  In set form,

\[
 B_{X_{t+1}}=
 \begin{cases}
  \{d_t\}\cup(B_{X_t}-\{c_t\}),&c_t\in B_{X_t},\\
  \{d_t\}\cup(B_{X_t}-\{\beta_H(X_t)\}),&c_t\notin B_{X_t}.
 \end{cases}                                                               \tag{2.6}
\]

The order in (2.4), which is stronger than (2.6), is essential at the next
bridge.  A promotion is exactly an early return of a cached departure; a
rotor step is an arrival from outside the cache.

This is the precise coupling missing from the two marginal flows.  The
lower flow chooses future departure queues; the upper flow chooses caches;
an owner edge is usable only when the target queues are exactly the two
updates (2.3)--(2.4).

## 3. Exact long-path coupling by residence

The preceding recurrence has a particularly clean solution on Johnson
cycles whose coordinates have sufficiently long residence.

Let \((X_t)_{t\in\mathbb Z/R\mathbb Z}\) be a directed Johnson cycle, with
departures and arrivals \(d_t,c_t\) as in (2.2), indices read cyclically.
Assume, for every \(t\), that

\[
 \begin{array}{ll}
 \text{(F)}&d_t,d_{t+1},\ldots,d_{t+H}\text{ are distinct and all belong
 to }X_t;\\[2mm]
 \text{(B)}&d_{t-1},\ldots,d_{t-H}\text{ are distinct and lie outside }X_t;\\[2mm]
 \text{(R)}&c_t\notin\{d_{t-1},\ldots,d_{t-H+1}\}.
 \end{array}                                                               \tag{3.1}
\]

Condition (R) permits \(c_t=d_{t-H}\).  This is return at exactly age
\(H\); every other permitted arrival is outside the whole upper cache.

### Theorem 3.1 (resident-cycle coupling lemma)

Under (3.1), define at every owner

\[
 \alpha(X_t)=(d_t,d_{t+1},\ldots,d_{t+H-1}),                                \tag{3.2}
\]

\[
 \beta(X_t)=(d_{t-1},d_{t-2},\ldots,d_{t-H}).                               \tag{3.3}
\]

Then these are valid full flags, and every cyclic arc
\(\omega_{X_t}\to\omega_{X_{t+1}}\) is bridge-one.  It is a last-position
promotion if \(c_t=d_{t-H}\), and a rotor shift otherwise.  Moreover, for
every \(0\le q\le H\),

\[
 \boxed{L_q(X_t)=\bigcap_{i=0}^qX_{t+i}},                                   \tag{3.4}
\]

\[
 \boxed{U_q(X_t)=\bigcup_{i=0}^qX_{t-i}.}                                   \tag{3.5}
\]

#### Proof

Conditions (F) and (B) make (3.2)--(3.3) ordered lists of distinct members
and nonmembers of \(X_t\), respectively.  The target lower word is

\[
 (d_{t+1},\ldots,d_{t+H}),
\]

and \(d_{t+H}\) lies in
\(X_t-\{d_t,\ldots,d_{t+H-1}\}\) by (F).  Thus (1.6) holds.  The target
upper word is

\[
 (d_t,d_{t-1},\ldots,d_{t-H+1}).                                           \tag{3.6}
\]

If \(c_t=d_{t-H}\), (3.6) is obtained from (3.3) by deleting its last
entry and prepending \(d_t\), so Theorem 1.1 gives last-position promotion.
Otherwise (R) says \(c_t\) is absent from (3.3), and the same queue update
is the rotor case of Theorem 1.1.

For (3.4), intersect successively with
\(X_{t+i+1}=X_{t+i}-d_{t+i}+c_{t+i}\).  Condition (F) says that each step
removes one new member of \(X_t\), so the intersection is

\[
 X_t-\{d_t,\ldots,d_{t+q-1}\}=L_q(X_t).
\]

Running the same identity backwards, adjoining \(X_{t-i}\) adds precisely
the old departure \(d_{t-i}\).  Condition (B) makes these \(q\) additions
distinct and absent from \(X_t\), proving (3.5). \(\square\)

Equations (3.4)--(3.5) are exactly the up-set path-hitting dictionary.  A
rank-\((m-q)\) target \(T\) is exposed at \(X_t\) precisely when the
forward \((q+1)\)-vertex segment lies in its principal up-set
\(\mathcal U_T\).  The upper statement is the complementary backward
path condition.  No reduction of arbitrary near-optimal OR words to
singleton U-cycles is being made: this is a sufficient construction inside
the declared resident-cycle architecture.

### 3.1 Recursive cube cycles

Take a recursive orientation-cube cycle of dimension \(\ell\), whose
transition word is \(\pi\pi\).  A toggled pair is not used again for
\(\ell\) steps.  If \(H\le\ell/2\), every block of \(H+1\) future
departures uses distinct pairs, every past departure remains absent for at
least \(H\) steps, and the current arrival is the mate in a new pair.
Thus (3.1) holds, every arc is a rotor arc, and Theorem 3.1 constructs a
coupled full flag at every owner.

The recursive half-depth injectivity theorem says additionally that, for
each \(q\le H\), the \(R=2\ell\) lower targets in one cycle are distinct,
and the \(R\) upper targets are distinct.  The exponential diversity of the
recursive coordinate orders is therefore fully available to CP.  It does
not remove the fixed-pair type deficit: cycles selected from many coordinate
pairings must still be coupled integrally.

### 3.2 The common-top promotion cycle

There is also an exact promotion solution of the same queue equations.
Fix a top \(U\in\binom{[n]}{m+H}\) and cyclically order its \(m+H\)
coordinates.  Let \(X_t\) run through the cyclic intervals of length \(m\).
The coordinate departing at time \(t\) returns at time \(t+H\), so
\(c_t=d_{t-H}\).  Theorem 3.1 gives a bridge-one cycle all of whose arcs
are last-position promotions.  Its lower and upper flags are the cyclic
intervals of lengths \(m-q\) and \(m+q\) in \(U\).

Equivalently, order \(L_X\) as \(\lambda_1,\ldots,\lambda_{m-H}\) and
form the role queue

\[
 (\lambda_1,\ldots,\lambda_{m-H},a_H,\ldots,a_1,b_1,\ldots,b_H).            \tag{3.7}
\]

Choose \(x=\lambda_{m-H}\), prepend \(b_H\) to the ordered lower base,
shift \(\alpha\), and prepend \(a_1\) to \(\beta\).  This is a one-place
rotation of (3.7).  The construction exactly couples the two flows inside
one common top, but Section 4 shows why it cannot dominate a CP solution.

## 4. CP requires a positive density of rotor arcs

For a full flag at \(X\), its depth-\(H\) upper target is its collar top

\[
 \mathsf U(X)=X\cup B_X\in\binom{[n]}{m+H}.                                 \tag{4.1}
\]

Promotion preserves \(\mathsf U\), while a rotor shift changes it by
deleting the old \(b_H\) and inserting the arriving residual coordinate.

### Theorem 4.1 (top-change lower bound)

Let a covering prefix transversal have a bridge-one path cover with \(p\)
components.  Let \(r\) be the number of internal arcs which are genuine
rotor shifts.  Then

\[
 \boxed{p+r\ge N_H.}                                                        \tag{4.2}
\]

#### Proof

On one path, the first state supplies one value of \(\mathsf U\).  Identity
and promotion arcs preserve that value; only a rotor arc can introduce a
new one.  Hence all paths together expose at most \(p+r\) distinct
rank-\((m+H)\) targets.  A covering prefix transversal exposes all \(N_H\)
such targets, proving (4.2). \(\square\)

For \(H=A\sqrt m+o(\sqrt m)\),

\[
 \frac{N_H}{W}\longrightarrow e^{-A^2}.                                    \tag{4.3}
\]

Therefore \(p=o(W/H)\) implies

\[
 r\ge (e^{-A^2}-o_A(1))W.                                                   \tag{4.4}
\]

In particular, a promotion-only path cover has \(p\ge N_H=\Theta_A(W)\).
The common-top construction of Section 3.2 is an exact local coupling and a
possible splice gadget, but it cannot provide the long global backbone.
The recursive mixed-frame rotor cycles have the correct qualitative
behavior: almost every internal step changes the top.

## 5. The symmetric fractional coupled-cycle solution

Let \(C\) be one resident cycle of length \(R\) whose owners are distinct
and whose lower and upper depth-\(q\) targets are distinct for every
\(q\le H\).  A recursive cube cycle with \(R=2\ell\) and
\(H\le\ell/2\) has these properties.  Take the indexed coordinate orbit

\[
 \mathscr O(C)=\{\sigma C:\sigma\in S_n\}.                                  \tag{5.1}
\]

Cut one arc in every cycle, but retain at each owner the cyclically defined
full flag.  This produces one bridge-one path per orbit column.

### Theorem 5.1 (exact fractional CP coupling)

Give every indexed orbit column the weight

\[
 \lambda=\frac{W}{n!R}.                                                      \tag{5.2}
\]

Then every middle owner has total weight exactly one.  At each depth
\(q\le H\), every lower target and every upper target has total flag weight

\[
 \boxed{\frac{W}{N_q}.}                                                      \tag{5.3}
\]

The total path weight is

\[
 \boxed{\frac WR.}                                                          \tag{5.4}
\]

#### Proof

The orbit contains \(n!R\) indexed owner occurrences.  Coordinate
transitivity makes their multiplicity constant over the \(W\) middle
owners, so a fixed owner occurs \(n!R/W\) times.  Multiplication by
\(\lambda\) gives weight one.

At depth \(q\), injectivity inside \(C\) gives \(R\) distinct lower target
occurrences and \(R\) distinct upper target occurrences per column.
Transitivity on either rank gives multiplicity \(n!R/N_q\) at a fixed
target.  Equation (5.3) follows from (5.2).  Finally there are \(n!\)
columns, proving (5.4). \(\square\)

Since \(W/N_q\ge1\), Theorem 5.1 satisfies every target-cover inequality
fractionally, not only the owner equations.  If \(H=o(R)\), then

\[
 \frac WR=o(W/H).                                                           \tag{5.5}
\]

This is an exact common fractional coupling of the lower and upper flows
along long bridge-one paths.  Because the orbit uses every coordinate
relabeling, it mixes pair frames and is not subject to the stationary-frame
Gaussian type deficit.

The slack at the deepest controlled rank is only constant:

\[
 \frac{W}{N_H}\longrightarrow e^{A^2}.                                     \tag{5.6}
\]

Thus the orbit identity alone does not turn an arbitrary integral rounding
into a covering transversal.  Zero deep-rank holes must be enforced during
the owner partition; there is no diverging target multiplicity that makes
this automatic.

## 6. The exact remaining integral discrepancies

There are two useful exact formulations: one directly on the two integral
flows, and one restricted to the recursive-cycle reservoir.

### 6.1 Ordered-Hall discrepancy after choosing the two flows

Let \(\mathcal F_{m,H}\) be the set of covering full-flag transversals:
one pair \((\alpha(X),\beta(X))\) at every owner, with every lower and upper
target through depth \(H\) covered.  The balanced transversals furnished by
Theorem 4.8 form a nonempty subset \(\mathcal F^{\rm bal}_{m,H}\).

For \(F\in\mathcal F_{m,H}\), let \(\Gamma_F\) be the directed owner graph
whose arcs are exactly those satisfying (1.5)--(1.7).  For a total order
\(\prec\) of the owners, retain only the forward arcs and form the split
bipartite graph \(B(F,\prec)\).  Define

\[
 \Delta(F,\prec)=
 \max_{\mathcal A\subseteq\binom{[n]}m}
 \bigl(|\mathcal A|-|N_{B(F,\prec)}(\mathcal A)|\bigr).                     \tag{6.1}
\]

By the deficiency form of Hall's theorem, a maximum matching in
\(B(F,\prec)\) leaves exactly \(\Delta(F,\prec)\) path starts.  Conversely,
every directed path cover can be made forward in some total order.  Hence

\[
 \boxed{
 p^*_{\rm CP}(m,H)=
 \min_{F\in\mathcal F_{m,H}}
 \min_{\prec}\Delta(F,\prec).}                                             \tag{6.2}
\]

In particular, \(\mathrm{CP}_A\) is exactly

\[
 p^*_{\rm CP}(m,H)=o_A(W/H).                                                \tag{6.3}
\]

The stronger balanced-flow attack requested here is the sufficient gate

\[
 \boxed{
 \min_{F\in\mathcal F^{\rm bal}_{m,H}}
 \min_{\prec}\Delta(F,\prec)=o_A(W/H).}                                    \tag{BCP_A}
\]

The content of Theorem 1.1 is that the neighbor set in (6.1) is now fully
explicit in the two flow words.  It requires the \((H-1)\)-symbol lower
overlap (1.6) and the ordered upper-cache update (1.7).  Separate
floor/ceiling balance supplies neither condition.

### 6.2 Recursive mixed-frame cycle rounding

Let \(\mathscr P_{\rm rec}\) contain all coordinate relabelings of all
cyclic subpaths of the recursive resident cycles.  Each state of a subpath
retains the full cyclic flag (3.2)--(3.3), even at the two cut endpoints.
For \(P\in\mathscr P_{\rm rec}\), write

\[
 m_{X,P}=\mathbf1_{\{X\text{ is an owner of }P\}},                          \tag{6.4}
\]

and let \(h^-_{T,P}\), respectively \(h^+_{T,P}\), indicate that one of
its owner flags equals the lower target \(T\), respectively the upper target
\(T\).  Define

\[
 \begin{split}
 \mathfrak C_{m,H,\ell}=\min\Bigl\{&\sum_{P\in\mathscr P_{\rm rec}}z_P:\\
 &\sum_Pm_{X,P}z_P=1
       &&\bigl(X\in\tbinom{[n]}m\bigr),\\
 &\sum_Ph^-_{T,P}z_P\ge1
       &&\bigl(T\in\tbinom{[n]}{m-q},\ 1\le q\le H\bigr),\\
 &\sum_Ph^+_{T,P}z_P\ge1
       &&\bigl(T\in\tbinom{[n]}{m+q},\ 1\le q\le H\bigr),\\
 &z_P\in\mathbb Z_{\ge0}\Bigr\}.
 \end{split}                                                               \tag{6.5}
\]

The middle equations force chosen paths to be owner-disjoint.  The target
inequalities say that their inherited flags form a covering prefix
transversal.  Therefore

\[
 \boxed{\mathfrak C_{m,H,\ell}=o_A(W/H)}                                    \tag{RCCP_A}
\]

for some \(\ell\) with \(H=o(\ell)\le m\) is a concrete sufficient theorem
for \(\mathrm{CP}_A\).

If (6.5) is relaxed to nonnegative real variables and full \(R\)-cycles
are allowed, Theorem 5.1 gives the feasible point

\[
 \sum_P z_P=\frac WR=o(W/H).                                                \tag{6.6}
\]

Thus \((\mathrm{RCCP}_A)\) is a pure integrality gap.  Whole cycles alone
already show the first scalar discrepancy: their exact owner partition
would require

\[
 R\mid W.                                                                  \tag{6.7}
\]

Allowing a polynomial number of residual subpaths removes (6.7) at
negligible path cost, but does not solve the individual owner equations and
all target-cover inequalities simultaneously.  Unlike the earlier SCD
semigroup gate, (6.5) has no rank-census or shadow-disjointness constraint;
only middle ownership, target coverage, and path count remain.

## 7. Audit of what has and has not been proved

The following points are proved in this note.

* Bridge-one compatibility of two full flags is exactly (1.5)--(1.7).
* Along a long path, lower deletion words are future-departure windows and
  upper addition words obey the cache recurrence (2.4).
* Resident Johnson cycles give an exact integral coupling along every
  internal arc, with flags equal to consecutive intersections and unions.
* Recursive cube cycles satisfy the residence and injectivity hypotheses.
* The complete mixed coordinate orbit is a fractional covering owner
  partition of path weight \(W/R=o(W/H)\).
* Any CP solution with low path count needs \(\Theta_A(W)\) rotor arcs.

The following implication is not proved.

\[
 \text{two separately balanced integral flows}
 \quad\Longrightarrow\quad
 \text{a low-component bridge-one path cover}.                              \tag{7.1}
\]

The exact missing datum is the common integral chronology encoded either by
the ordered-Hall deficit (6.1)--(6.3) or, in the recursive mixed-frame
architecture, by (6.5).  The most focused next lemma is therefore:

> **Mixed-frame coupled-cycle rounding lemma.**  For
> \(H=A\sqrt m+o(\sqrt m)\), choose a power of two \(\ell\asymp m\).
> The symmetric fractional point of Theorem 5.1 can be rounded, using
> recursive cycles and residual subpaths, to (6.5) with
> \(\sum_Pz_P=o_A(W/H)\).

This lemma would prove \(\mathrm{CP}_A\) directly.  It explicitly permits
the coordinate pairing to depend on the selected long path, so it respects
the fixed-frame Gaussian deficit.  What remains is a correlated integral
rounding of the middle-owner equations and the lower/upper path-hitting
inequalities, not an SCD resolution and not a promotion-fibre construction.
