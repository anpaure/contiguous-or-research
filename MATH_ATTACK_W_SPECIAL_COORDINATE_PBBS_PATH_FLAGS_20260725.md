# Lane W: special-coordinate PBBS paths, balanced depth one, and the cap obstruction

Date: 2026-07-25

Method: pure mathematics only.  No generic Johnson compiler, computation,
solver, or probabilistic rounding theorem is used.

## 0. Exact verdict

Let

\[
 Q=[2m],\qquad
 W=\binom{2m}{m},\qquad
 B=\operatorname {Cat}_m={W\over m+1},
 \qquad H<m.
 \tag{0.1}
\]

Fix an exact odd wreath factor on \(Q\cup\{\infty\}\), and cut every
wreath at its unique edge omitted by \(\infty\).  The resulting
\(B\) complementary Johnson geodesics have \(m+1\) owners each and
partition \(\binom Qm\).

This restriction gives a genuine positive theorem beyond a flow
reformulation.

1. **Full chronology is solved.**  For every orientation of every path and
   every \(H<m\), there is an explicit full radius-\(H\) useful state above
   every owner, and all \(m\) owner transitions are bridge one.  Thus the
   entire even middle layer has a bridge-one path cover with exactly
   \[
     \boxed{p=B={W\over m+1}=o(W/H)}
     \tag{0.2}
   \]
   whenever \(H=o(m)\), in particular for
   \(H=\lceil A\sqrt m\rceil\).
2. **The upper depth-one flags can always be made exactly balanced.**  Every
   rank-\((m+1)\) target occurs once, and exactly \(B\) distinct targets
   occur a second time.
3. **The lower depth-one flags have an exact two-choice cap criterion.**
   The \(mB=\binom{2m}{m-1}\) internal path meets are fixed.  Orienting one
   path chooses exactly one of its two endpoint caps as the remaining lower
   flag.  Exact balance is therefore a capacitated bipartite matching with
   one binary choice per path.
4. **Failure is exactly a PBBS shadow-load obstruction before Hall enters.**
   A rank-\((m-1)\) target is absent from the lower chronological flags for
   every orientation if and only if its non-\(\infty\) depth-one shadow load
   in the original odd wreath factor is zero.
5. **The canonical MSW/PBBS factor fails this test.**  At \(m=4\), with
   \(\infty=9\), the two targets
   \[
      \{1,4,7\},\qquad \{2,5,8\}
      \tag{0.3}
   \]
   have zero non-special PBBS shadow load.  Hence every special-coordinate
   path restriction of that oriented factor misses both targets, even
   after the best endpoint-cap choices.  Thus the unchanged canonical
   factor does not prove even the depth-one part of \((\mathrm{CP}_A)\).

The positive part is sharp: the path/bridge problem disappears completely,
and the first surviving obstruction is precisely the old PBBS/wreath
shadow load, followed by a small two-choice cap Hall problem.  A factor
rebundling which removes those holes would turn the same paths into an
exact depth-one balanced flag construction at no additional chronology
cost.

## 1. The fixed-coordinate complementary paths

Let \(F\) be an exact wreath factor on

\[
 Q\cup\{\infty\},\qquad |Q|=2m.
 \tag{1.1}
\]

Every wreath contains exactly one odd-graph edge whose omitted coordinate
is \(\infty\).  Cut that edge and retain the \(\infty\)-free owners.  One
obtains a Johnson geodesic

\[
 P=(X_0,X_1,\ldots,X_m),
 \qquad X_m=Q\setminus X_0,
 \tag{1.2}
\]

with

\[
 X_{t+1}=X_t-a_t+b_t.
 \tag{1.3}
\]

Since the endpoints are complementary and their Johnson distance is
\(m\),

\[
 (a_0,\ldots,a_{m-1})
 \tag{1.4}
\]

is an ordering of \(X_0\), while

\[
 (b_0,\ldots,b_{m-1})
 \tag{1.5}
\]

is an ordering of \(Q\setminus X_0\).  Put

\[
 w=(a_0,\ldots,a_{m-1},b_0,\ldots,b_{m-1}),
 \tag{1.6}
\]

read cyclically modulo \(2m\).  Then

\[
 \boxed{X_t=I_w(t,m)\qquad(0\le t\le m).}
 \tag{1.7}
\]

Across all \(B\) paths, the owner occurrences in (1.2) partition
\(\binom Qm\).  Moreover the internal joins

\[
 Y_t=X_t\cup X_{t+1}=I_w(t,m+1),
 \qquad0\le t<m,
 \tag{1.8}
\]

partition \(\binom Q{m+1}\).  This is the exact fixed-coordinate normal
form of an odd wreath factor.

For completeness, the second partition is not an extra property of the
chosen factor.  In the original cut odd cycle, the \(m\) owners containing
\(\infty\) are exactly

\[
 A_t=\{\infty\}\cup(Q\setminus Y_t),
 \qquad0\le t<m.
 \tag{1.9}
\]

Exact odd middle ownership makes all \(A_t\)'s over all factor cycles a
partition of the middle sets containing \(\infty\).  The map

\[
 Y\longmapsto\{\infty\}\cup(Q\setminus Y)
 \tag{1.10}
\]

is a bijection from \(\binom Q{m+1}\) onto that owner class.  Hence the
\(Y_t\)'s partition \(\binom Q{m+1}\) for every exact odd wreath factor.

## 2. An explicit full radius-\(H\) bridge lift

The lower queue has a canonical cyclic continuation.  At owner \(X_t\)
put

\[
 \alpha_t=(w_t,w_{t+1},\ldots,w_{t+H-1}).
 \tag{2.1}
\]

Because \(H<m\), all these coordinates are distinct members of the
length-\(m\) interval \(X_t\).  Its lower base is

\[
 L_t=I_w(t+H,m-H).
 \tag{2.2}
\]

For the upper queue, use the following **entry-neutral chord queue** at
the first owner:

\[
 \beta_0=(b_0,b_1,\ldots,b_{H-1}).
 \tag{2.3}
\]

All entries are distinct nonmembers of \(X_0\).  Propagate it by

\[
 \beta_t=
 \begin{cases}
 (a_{t-1},\ldots,a_0,b_t,\ldots,b_{H-1}),
       &0\le t\le H,\\[1mm]
 (a_{t-1},a_{t-2},\ldots,a_{t-H}),
       &H\le t\le m.
 \end{cases}
 \tag{2.4}
\]

The two formulas agree at \(t=H\).

### Theorem 2.1 (special-coordinate full-flag lift)

For every \(H<m\), the queues (2.1) and (2.4) define a full useful state
\(\omega_t\) above every \(X_t\), and

\[
 \boxed{\omega_t\longrightarrow\omega_{t+1}}
 \tag{2.5}
\]

is bridge one for all \(0\le t<m\).

The selected depth-one flags are

\[
 \boxed{
 L_1(X_t)=
 \begin{cases}
 X_t\cap X_{t+1},&t<m,\\
 X_m-b_0=Q\setminus Y_0,&t=m,
 \end{cases}}
 \tag{2.6}
\]

and

\[
 \boxed{
 U_1(X_t)=
 \begin{cases}
 Y_0,&t=0,\\
 X_{t-1}\cup X_t=Y_{t-1},&1\le t\le m.
 \end{cases}}
 \tag{2.7}
\]

#### Proof

The lower recurrence is immediate:

\[
 \alpha_{t+1}
 =(w_{t+1},\ldots,w_{t+H})
 \tag{2.8}
\]

is obtained from \(\alpha_t\) by deleting its first entry and appending
\(w_{t+H}\in L_t\).

For \(t<H\), the entering coordinate \(b_t\) occurs in (2.4).  Use the
singleton-promotion bridge which removes that entry from the upper queue
and prepends the departing coordinate \(a_t\).  This gives
\(\beta_{t+1}\).  For \(t\ge H\), \(b_t\) is in the residual upper block,
so use a rotor shift.  It prepends \(a_t\) and deletes the last old upper
marker, again giving (2.4).  The lower base update is

\[
 L_{t+1}=L_t-w_{t+H}+b_t,
 \tag{2.9}
\]

with the evident cyclic interpretation after \(t=m-H\).  Thus every
transition is one of the exact bridge-one cases.

Equations (2.6)--(2.7) follow by taking the first entries of
\(\alpha_t\) and \(\beta_t\).  At \(t=m\), the first lower departure is
\(w_m=b_0\), while at \(t=0\) the first upper marker is the same
coordinate. \(\square\)

### Corollary 2.2 (the path-count gate is solved)

The complete special-coordinate restriction has a full-state bridge-one
path cover with exactly

\[
 p=B={W\over m+1}
 \tag{2.10}
\]

components.  Its exact useful-prefix length is

\[
 \boxed{W+2HB.}
 \tag{2.11}
\]

For \(H=\lceil A\sqrt m\rceil\),

\[
 {2HB\over W}={2H\over m+1}=O_A(m^{-1/2})=o(1).
 \tag{2.12}
\]

Thus only target coverage remains; no nonlocal component fusion is needed
for this restricted construction.

## 3. An unconditional exactly balanced upper first band

Let

\[
 N_1=\binom{2m}{m+1}=\binom{2m}{m-1}=mB.
 \tag{3.1}
\]

There are \(W=(m+1)B\) advertised upper depth-one flags.  Exact balance
therefore means that every rank-\((m+1)\) target has load one or two, with
exactly \(B\) targets of load two.

### Theorem 3.1 (upper depth-one balance)

The upper flags (2.7), over all restricted paths, are exactly balanced.

#### Proof

By the fixed-coordinate normal form, the \(mB=N_1\) internal unions
\(Y_t\) in (1.8) enumerate \(\binom Q{m+1}\) exactly once.  Equation
(2.7) advertises all of them at the target owners \(X_1,\ldots,X_m\).

At the initial owner of each path it advertises \(Y_0\) once more.  The
\(Y_0\)'s belonging to different paths are distinct because the complete
internal union family is a partition.  Hence precisely those \(B\) targets
have load two, and every other target has load one. \(\square\)

This proof is orientation-independent.  Reversing one path replaces its
first edge union by the old last edge union, but still selects one member of
that path's internal union family.  Since the complete internal family is a
global partition, arbitrary independent path reversals still select
\(B\) distinct duplicated targets.  The queue formulas are reapplied with
the reversed \(a\)- and \(b\)-lists; the same promotion/rotor induction is
unchanged.

This is a genuine balanced flag theorem, not merely coverage and not a
fractional statement.

## 4. The lower first band is a two-choice cap matching

For one unoriented path put

\[
 E_0(P)=Q\setminus Y_0,
 \qquad
 E_1(P)=Q\setminus Y_{m-1}.
 \tag{4.1}
\]

They are its two rank-\((m-1)\) endpoint caps.  In the orientation used in
Sections 1--3, the terminal flag in (2.6) is \(E_0(P)\).  Reversing the
path gives the same internal meet multiset and chooses \(E_1(P)\) instead.

For \(S\in\binom Q{m-1}\), define the internal meet load

\[
 d(S)=\#\{(P,t):0\le t<m, X_t\cap X_{t+1}=S\}.
 \tag{4.2}
\]

An orientation selector

\[
 \varepsilon:\mathcal P\longrightarrow\{0,1\}
 \tag{4.3}
\]

has lower flag load

\[
 \boxed{
 \lambda^-_1(S;\varepsilon)
 =d(S)+\#\{P:E_{\varepsilon(P)}(P)=S\}.}
 \tag{4.4}
\]

### Theorem 4.1 (exact entry-neutral cap criterion)

The restricted paths admit an exactly balanced lower depth-one flag table
if and only if the two-choice bipartite graph

\[
 P\sim E_0(P),E_1(P)
 \tag{4.5}
\]

has a left-perfect integral \(b\)-matching in which target \(S\) has degree
in the interval

\[
 \boxed{
 \ell(S)=\max\{0,1-d(S)\},
 \qquad
 u(S)=2-d(S).}
 \tag{4.6}
\]

In particular, \(d(S)>2\) is an immediate obstruction.  Subject to
\(d(S)\le2\), feasibility is characterized exactly by the lower-bounded
max-flow, or equivalently by Hoffman's cut inequalities for the network

\[
 s\longrightarrow\mathcal P
 \longrightarrow\binom Q{m-1}longrightarrow t
 \tag{4.7}
\]

with unit path capacities and target intervals (4.6).

For mere coverage, the exact condition is a matching which assigns every
target with \(d(S)=0\) to a distinct incident path.  Equivalently,

\[
 \boxed{
 |N(\mathcal H)|\ge|\mathcal H|
 \quad
 \text{for every family }
 \mathcal H\subseteq\{S:d(S)=0\}.}
 \tag{4.8}
\]

#### Proof

Every path contributes exactly one terminal cap, and (4.4) is the complete
lower flag list.  Since

\[
 {W\over N_1}={m+1\over m}\in(1,2),
 \tag{4.9}
\]

exact balance is precisely \(1\le\lambda^-_1(S)\le2\) for every target.
Subtracting the fixed load \(d(S)\) gives (4.6).  Choosing one cap from
each path is a left-perfect \(b\)-matching, proving the first assertion.
Integral max-flow and Hoffman's theorem give (4.7).

For coverage only, a target with \(d(S)>0\) needs no cap.  Every target
with \(d(S)=0\) must receive a cap, one path cannot supply two caps, and
extra caps may be arbitrary.  Hall's theorem gives (4.8). \(\square\)

The theorem is the promised entry-neutral chord/cut closure: the chosen
cap is installed by the terminal continuation in (2.1), while the matching
upper duplicate is installed by the initial queue (2.3).  Neither requires
an extra owner, bridge, reset, or QCF chart.

## 5. Exact equivalence with the PBBS shadow load

Rotate one odd wreath so that its omitted-label/cyclic-coordinate word is

\[
 (\infty,a_0,\ldots,a_{m-1},b_0,\ldots,b_{m-1}).
 \tag{5.1}
\]

The rank-\((m-1)\) odd-wreath shadows not containing \(\infty\) are
exactly

\[
 X_t\cap X_{t+1}quad(0\le t<m),
 \qquad E_0(P),\ E_1(P).
 \tag{5.2}
\]

This is the fixed-coordinate PBBS shadow formula.  Define its load by

\[
 \mu_{F,\infty}^{0}(S)
 =d(S)
  +\#\{P:E_0(P)=S\}
  +\#\{P:E_1(P)=S\}.
 \tag{5.3}
\]

### Theorem 5.1 (absolute restricted hole iff PBBS shadow hole)

For every \(S\in\binom Q{m-1}\), the following are equivalent.

1. \(S\) is absent from the chronological lower depth-one flags for every
   orientation of all restricted paths.
2. \(S\) is neither an internal meet nor either endpoint cap of any path.
3. \[
      \boxed{\mu_{F,\infty}^{0}(S)=0.}
      \tag{5.4}
   \]

#### Proof

By (4.4), the union of the possible lower flags over both orientations of
one path is its internal meet family together with both caps.  Taking the
union over all paths proves the equivalence of 1 and 2.  Formula (5.3)
proves the equivalence with 3. \(\square\)

Thus the special-coordinate restriction does not create a new mysterious
coverage problem.  Its orientation-independent holes are exactly the
non-special PBBS shadow holes of the original odd factor.  If none exist,
the only remaining depth-one issue is the explicit cap Hall condition
(4.8), or its balanced version (4.6).

## 6. Canonical MSW/PBBS obstruction

For the canonical MSW factor at \(m=4\), take

\[
 Q=[8],\qquad\infty=9.
 \tag{6.1}
\]

The exact odd-wreath depth-one shadow calculation gives four holes

\[
 \{1,4,7\},\quad
 \{2,5,8\},\quad
 \{2,5,9\},\quad
 \{4,7,9\}.
 \tag{6.2}
\]

The first two avoid \(\infty\).  Therefore

\[
 \mu_{F,9}^{0}(\{1,4,7\})
 =\mu_{F,9}^{0}(\{2,5,8\})=0.
 \tag{6.3}
\]

### Corollary 6.1 (unchanged canonical restriction fails depth one)

For \(m=4\), every orientation of the \(14\) special-coordinate paths and
every entry-neutral endpoint-cap choice misses the two lower targets in
(6.3).  Consequently the selected full flags are not a covering prefix
transversal, and in particular are not balanced.

#### Proof

Apply Theorem 5.1. \(\square\)

This finite obstruction disproves the assertion that exact odd ownership,
complementary endpoints, or the upper edge-color bijection automatically
gives balanced even flags.  It does not disprove the existential strategy
of replacing the canonical factor by a different exact odd wreath factor.

## 7. Higher-depth boundary

For the cyclic lower continuation (2.1), every depth \(q\le H\) lower flag
is

\[
 \boxed{L_q(X_t)=I_w(t+q,m-q).}
 \tag{7.1}
\]

Thus its complete load is the exact half-row PBBS interval load

\[
 \lambda_q^-(S)
 =\#\{(P,t):0\le t\le m, I_{w(P)}(t+q,m-q)=S\}.
 \tag{7.2}
\]

There is no theorem forcing (7.2) to cover, let alone balance, every
rank-\((m-q)\) target.  At \(q=1\), Sections 4--6 give its complete
two-cap decision.  At larger \(q\), reversing a path changes an ordered
\(q\)-cap, and the choices at different depths are nested.  The exact
remaining problem is therefore a coupled multi-depth cap matching, not a
path-lift problem.

The entry chord (2.3) has a useful warning.  For \(0\le t\le q\le H\), its
upper flag is

\[
 U_q(X_t)
 =X_0\cup\{b_0,\ldots,b_{q-1}\},
 \tag{7.3}
\]

independent of \(t\).  Hence one path contributes \(q+1\) identical upper
boundary flags at depth \(q\).  This is harmless at \(q=1\), where it is
exactly one allowed duplicate, but for \(q\ge2\) it may exceed the
balanced ceiling.  Thus the entry-neutral depth-one chord is not promoted
to an all-depth balanced chord.

### 7.1 All legal terminal continuations

The two endpoint caps in Section 4 describe the particular cyclic lower
continuation (2.1), not all full-radius bridge lifts of the intact path.
There is a larger exact list.

Let \(c=(c_0,\ldots,c_{H-1})\) be an ordered list of distinct members of
\(X_m=\{b_0,\ldots,b_{m-1}\}\), viewed as formal removals after the \(m\)
physical path edges.

### Proposition 7.1 (exact lower terminal-list theorem)

The list \(c\) extends the forced physical deletion queues to a full
radius-\(H\) bridge lift if and only if

\[
 \boxed{
 c_d\in\{b_0,\ldots,b_{m-H+d-1}\}
 \setminus\{c_0,\ldots,c_{d-1}\}
 \qquad(0\le d<H).}
 \tag{7.4}
\]

Put

\[
 r=(a_0,\ldots,a_{m-1},c_0,\ldots,c_{H-1}).
 \tag{7.5}
\]

Then every lower queue is

\[
 \alpha_t=(r_t,r_{t+1},\ldots,r_{t+H-1}),
 \qquad0\le t\le m.
 \tag{7.6}
\]

If \(t+q\le m\), the depth-\(q\) lower flag remains the forced internal
interval \(I_w(t+q,m-q)\).  If \(t=m-k\) with \(0\le k<q\), its boundary
value is

\[
 \boxed{
 L_q(X_{m-k})
 =\{b_0,\ldots,b_{m-k-1}\}
  \setminus\{c_0,\ldots,c_{q-k-1}\}.}
 \tag{7.7}
\]

#### Proof

The physical transition at edge \(t<m\) removes \(a_t\).  The bridge queue
law therefore forces the entries \(a_t,a_{t+1},\ldots,a_{m-1}\), followed
by one common terminal continuation.  The entry \(c_d\) is appended at
physical edge \(m-H+d\).  At that owner the lower residual block is

\[
 \{b_0,\ldots,b_{m-H+d-1}\}
 \setminus\{c_0,\ldots,c_{d-1}\}.
\]

Thus the bridge requirement \(c_d\in L\) is exactly (7.4).  Conversely,
(7.4) makes every append legal, so the queue recurrence gives (7.6).
Deleting its first \(q\) entries gives (7.7). \(\square\)

At depth one the complete legal terminal list is

\[
 \boxed{\mathcal L_H(P)=\{X_m-b_j:0\le j<m-H\}.}
 \tag{7.8}
\]

Every member extends to a full continuation: after fixing \(c_0\), the
allowed set at step \(d\) has size \(m-H+d\ge d+1\), so greedy distinct
representatives suffice.

### Corollary 7.2 (exact all-lift lower first-band gate)

For fixed orientations of the intact paths, the lower depth-one flags are
exactly balanced among all full-radius-\(H\) bridge lifts if and only if
the list graph

\[
 P\sim\mathcal L_H(P)
 \tag{7.9}
\]

has a left-perfect integral \(b\)-matching with target interval

\[
 \left[\max\{0,1-d(S)\},\,2-d(S)\right].
 \tag{7.10}
\]

For coverage alone, every target with \(d(S)=0\) must be matched to a
distinct incident path.  In particular, if

\[
 h_1^{\rm int}=|\{S:d(S)=0\}|,
 \tag{7.11}
\]

then

\[
 \boxed{h_1^{\rm int}>B
 \Longrightarrow
 \text{no full-radius lift of these intact paths covers depth one}.}
 \tag{7.12}
\]

Every nonterminal first flag is the forced meet of its outgoing edge,
while Proposition 7.1 gives exactly one listed terminal flag per path.
This proves the matching criterion and the capacity obstruction.  The
two-cap graph (4.5) is exact for the cyclic continuation and its reversal,
but is not an obstruction to all endpoint queues.

### 7.2 The upper first band is always solvable

### Theorem 7.3 (unconditional upper depth-one completion)

For any fixed orientations of the \(B\) complementary paths, the initial
upper queues can be chosen so that the complete upper depth-one table is
exactly balanced.  This choice is independent of every legal lower
continuation in Proposition 7.1.

#### Proof

The \(mB=\binom{2m}{m+1}\) flags at noninitial owners are the internal
unions \(Y_t\), which enumerate every target once.  It remains to choose
distinct upper neighbors of the \(B\) initial owners.

For a subfamily \(\mathcal A\) of initial owners,

\[
 |\mathcal A|\le B={1\over m+1}\binom{2m}m
 \le {1\over2}\binom{2m}m.
 \tag{7.13}
\]

Complementing turns its upper shadow into the lower shadow of a family of
\(m\)-sets of the same size.  Write
\(|\mathcal A|=\binom xm\) in Lovasz form.  Then \(x\le2m-1\), so

\[
 |\partial^+\mathcal A|
 \ge\binom{x}{m-1}
 =\binom xm{m\over x-m+1}
 \ge|\mathcal A|.
 \tag{7.14}
\]

Hall's theorem assigns distinct supersets \(U(P)\supset X_0(P)\).  Put
the coordinate \(U(P)\setminus X_0(P)\) first in \(\beta_0(P)\) and
complete the cache arbitrarily.  Bridge propagation is always a legal
promotion or rotor.  The distinct \(U(P)\)'s are precisely the \(B\)
duplicated targets. \(\square\)

### 7.3 A one-promotion collar

The initial cache

\[
 \beta_0=(b_0,b_{m-1},b_{m-2},\ldots,b_{m-H+1})
 \tag{7.15}
\]

promotes \(b_0\) at edge zero and uses rotors thereafter.  It gives

\[
 \beta_t=(a_{t-1},\ldots,a_0,b_{m-1},\ldots,b_{m-H+t})
 \quad(1\le t\le H),
 \tag{7.16}
\]

and \(\beta_t=(a_{t-1},\ldots,a_{t-H})\) for \(t\ge H\).
For \(1\le t<q\le H\),

\[
 U_q(X_t)
 =X_0\cup\{b_0,\ldots,b_{t-1}\}
       \cup\{b_{m-q+t},\ldots,b_{m-1}\},
 \tag{7.17}
\]

while

\[
 U_q(X_0)
 =X_0\cup\{b_0\}\cup\{b_{m-q+1},\ldots,b_{m-1}\},
 \tag{7.18}
\]

and \(U_q(X_t)=I_w(t-q,m+q)\) for \(t\ge q\).  Hence \(t=0,1\)
give the only equal pair inside one path.  At depth one the list is

\[
 Y_0,Y_0,Y_1,\ldots,Y_{m-1},
 \tag{7.19}
\]

so it is globally exactly balanced.  At higher depth this removes the old
within-path multiplicity \(q+1\), but cross-path collisions and interval
coverage remain open.

A successful Gaussian-depth theorem must choose the entire initial upper
queue and terminal lower queue jointly across paths so that all nested cap
loads balance.  The chronology and component ledger are already solved by
Theorem 2.1 and Corollary 2.2.

## 8. Proved/remaining ledger

### Proved

1. Every special-coordinate complementary path has the explicit full
   radius-\(H\) bridge lift (2.1)--(2.4).
2. The complete even owner layer has exactly \(B=W/(m+1)\) bridge-one
   paths and literal excess \(2HB=o(W)\) in the Gaussian window.
3. The upper depth-one flags can always be made exactly balanced.
4. For the cyclic continuation and its reversal, lower depth-one balance
   is exactly the two-choice capacitated matching (4.6).  Among all
   full-radius endpoint continuations, it is the larger Ferrers-list
   matching (7.9)--(7.10).
5. Orientation-independent lower holes are exactly zero non-special PBBS
   shadow loads.
6. The unchanged canonical MSW/PBBS factor fails this test already at
   \(m=4\).
7. The natural entry chord creates \(q+1\) repeated higher-depth boundary
   flags.  The single-promotion collar (7.15) reduces this to one duplicate
   pair while preserving exact upper depth-one balance.
8. Independently of a canonical collar, the initial upper queues always
   admit an exactly balanced depth-one completion by Theorem 7.3.

### Remaining exact theorem

Find an exact odd wreath factor and, on each special-coordinate path, one
pair of full endpoint queues such that the nested lower and upper cap loads
through \(H=\lceil A\sqrt m\rceil\) cover every target (or are balanced).
No additional path-cover estimate is required: the same construction then
has

\[
 W+2H\operatorname {Cat}_m=W+o_A(W)
 \tag{8.1}
\]

literal length.  For the canonical factor, the PBBS shadow holes in
Section 6 show that endpoint queues alone cannot suffice without changing
the underlying wreath rows.
