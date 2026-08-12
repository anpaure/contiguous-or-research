# Pascal reroot and owner-oriented common-cap compiler

Date: 2026-07-31  
Lane: K, all-\(k\) construction extracted from the optimal \(k=16\) word  
Status: the abstract implications below are proved; their uniform hypotheses
for every \(k\) remain open

## 1. Purpose and scope

The authenticated \(k=16\) construction has four logically separate parts:

1. a one-defect Pascal lift of an odd parent;
2. two endpoint reroots which absorb the missing upper rays;
3. a monotone depth-\(d\) schedule, retimed to expose a scarce singleton;
4. an integral lower-cell matching whose **joint** maximal cap is literal.

This note extracts a reusable theorem from those four parts. It does not use
the now-closed \(k=16\) basin as evidence for an unproved all-\(k\) assertion.
In particular, no marginal Hall condition is promoted to common-cap
sufficiency.

Throughout, a word is a sequence of nonempty subsets and the value of an
interval is their union.

## 2. One-defect Pascal lift

Let \(\Omega\) have size \(2r-1\), let \(z\notin\Omega\), and put

\[
        N=\binom{2r-1}{r}=\binom{2r-1}{r-1}.
\]

For a word \(w=(w_0,\ldots,w_{N+h-1})\) on \(\Omega\), define

\[
 Q_i=\bigcup_{t=0}^{h}w_{i+t}\quad(0\le i<N),
 \qquad
 P_i=\bigcup_{t=0}^{h-1}w_{i+t}\quad(0\le i\le N).
\tag{2.1}
\]

### Lemma 2.1 (one-defect Pascal middle lift)

Assume:

1. \(Q_0,\ldots,Q_{N-1}\) are the \(r\)-subsets of \(\Omega\), each once;
2. for one index \(c\), \(P_c\) is not of rank \(r-1\);
3. the other \(N\) values \(P_i\), \(i\ne c\), are the
   \((r-1)\)-subsets of \(\Omega\), each once.

Then

\[
 \operatorname{rev}(z\cup P_{[0,c)})
 \ \Vert\ (Q_0,\ldots,Q_{N-1})\
 \Vert\ \operatorname{rev}(z\cup P_{(c,N]})
\tag{2.2}
\]

is a permutation of all \(r\)-subsets of \(\Omega\cup\{z\}\).
The \(Q\)-block may be split into any number of consecutive subblocks without
changing this conclusion.

#### Proof

The \(Q_i\) are exactly the \(r\)-sets avoiding \(z\). The marked values
\(z\cup P_i\), \(i\ne c\), are exactly the \(r\)-sets containing \(z\).
These Pascal shores are disjoint and have total size

\[
 \binom{2r-1}{r}+\binom{2r-1}{r-1}=\binom{2r}{r}.
\]

Reversal and consecutive block splitting only change order. Thus (2.2) is
the complete middle layer. \(\square\)

This lemma asserts middle ownership only. Johnson adjacency, residence,
upper shadows, and compilation require separate hypotheses.

## 3. Exact endpoint-ray reroot

Let \(T=(T_0,\ldots,T_{W-1})\) be any middle-layer permutation. Choose
\(0\le a<a+1<b<W\), so all three blocks below are nonempty, and define

\[
 T^{a,b}
 =\operatorname{rev}(T_{[0,a]})
  \ \Vert\ T_{[a+1,b)}
  \ \Vert\operatorname{rev}(T_{[b,W)}).
\tag{3.1}
\]

### Lemma 3.1 (two-boundary law)

The unordered adjacent-pair multiset changes only as follows:

\[
\begin{aligned}
 \{T_a,T_{a+1}\}&\longrightarrow\{T_0,T_{a+1}\},\\
 \{T_{b-1},T_b\}&\longrightarrow\{T_{b-1},T_{W-1}\}.
\end{aligned}
\tag{3.2}
\]

Consequently the \(q=1\) upper-colour multiset changes by replacing only the
two corresponding unions.

#### Proof

Every pair internal to one of the three blocks remains the same unordered
pair after reversal. The two displayed block boundaries are the only new
adjacencies. \(\square\)

For deeper targets, let \(\mathcal I(B)\) be the interval-union set of a
block \(B\). Let \(\mathcal R_{a,b}\) contain the unions in \(T^{a,b}\) of
intervals crossing at least one block boundary. It is generated exactly by
an original prefix and a prefix of the middle block, a suffix of the middle
block and an original suffix, or one object of each type together with the
whole middle block.

### Corollary 3.2 (ray absorption criterion)

If every required upper target belongs to

\[
 \mathcal I(\operatorname{rev}T_{[0,a]})
 \cup\mathcal I(T_{[a+1,b)})
 \cup\mathcal I(\operatorname{rev}T_{[b,W)})
 \cup\mathcal R_{a,b},
\tag{3.3}
\]

then \(T^{a,b}\) is upper-complete. In particular, it suffices that every old
target without an internal-block witness has a new ray witness and that the
new rays contain every old deficit.

This is an exact finite condition. Merely installing the two missing
\(q=1\) colours does not imply (3.3).

## 4. Monotone schedules and frozen prepins

Let \(T_0,\ldots,T_{W-1}\) be rank-\(r\) targets. Assign row \(i\) a physical
interval \(I_i=[s_i,e_i]\subseteq[0,L-1]\), with both endpoint sequences
strictly increasing. Assume

\[
 |I_i|\le d+1,\qquad s_{i+1}\le e_i+1.
\tag{4.1}
\]

Define

\[
        E_p=\bigcap_{i:p\in I_i}T_i.
\tag{4.2}
\]

Assume \(E_p\ne\varnothing\) and

\[
        \bigcup_{p\in I_i}E_p=T_i\quad\text{for every }i.
\tag{4.3}
\]

Let \(\mathcal C\) be a catalogue of physical lower cells, each an interval
of length at most \(d\).

A **prepin bank** is an injection \(\pi:\mathcal P\to\mathcal C\) from some
lower targets to cells. Set

\[
 \bar E_p=E_p\cap
          \bigcap_{\substack{S\in\mathcal P\\p\in\pi(S)}}S.
\tag{4.4}
\]

### Lemma 4.1 (prepin freezing)

If all \(\bar E_p\) are nonempty, every middle row remains exact, and every
prepin cell has union equal to its assigned target, then the bank may be
frozen into the pointwise envelope.  During the residual assignment, however,
every multi-cell prepin equality remains a protected row.  A one-cell
singleton prepin is automatic once nonemptiness is protected.

#### Proof

Every later cap is an additional intersection, so (4.4) records exactly the
pointwise restriction imposed by the bank.  A later cap overlapping a
multi-cell prepin can nevertheless delete its last provider for some bit.
Keeping each prepin equality among the residual protected rows is therefore
necessary and sufficient.  If the prepin is a one-cell singleton, every
nonempty final submask of that cell equals the singleton, so no separate
bit-row is needed. \(\square\)

This is the reusable form of singleton retiming. It applies to any finite
bank of scarce targets, not only to one singleton.

## 5. Maximal common cap

For a residual lower target \(S\), let a candidate incidence be a pair
\(e=(S,C)\), \(C\in\mathcal C\), which is individually exact relative to
\(\bar E\): capping \(C\) by \(S\) alone leaves every letter nonempty,
replays every middle and protected-prepin row, and gives union \(S\) on
\(C\).  Equivalently, begin with all local incidences and delete every unary
conflict. Let \(M\) choose one distinct cell for every residual target.
Define

\[
 A_p(M)=\bar E_p\cap
        \bigcap_{\substack{S\\p\in M(S)}}S.
\tag{5.1}
\]

### Theorem 5.1 (maximal-cap criterion)

The residual assignment \(M\), together with the middle rows and protected
prepin bank, has a simultaneous physical realization relative to \(\bar E\)
if and only if

1. \(A_p(M)\ne\varnothing\) for every \(p\);
2. \(\bigcup_{p\in I_i}A_p(M)=T_i\) for every middle row;
3. \(\bigcup_{p\in M(S)}A_p(M)=S\) for every residual lower target;
4. \(\bigcup_{p\in\pi(U)}A_p(M)=U\) for every protected multi-cell prepin
   \(U\).

When these conditions hold, \(A(M)\) itself is the maximal realization.

#### Proof

Any realizing word \(B\) must be contained in every active middle target,
every protected prepin, and every lower target whose chosen cell contains
\(p\). Hence
\(B_p\subseteq A_p(M)\). Enlarging \(B\) to \(A(M)\) cannot lose a required
bit, while (4.4)--(5.1) forbid every bit outside an assigned middle, prepin,
or lower target. This proves necessity and sufficiency. \(\square\)

Because of (4.1), the physical union of any consecutive block of middle rows
is an interval. Therefore, if \(T\) is upper-complete, conditions 1--4 make
\(A(M)\) universal.

## 6. The exact bounded-rank obstruction hypergraph

Make every candidate incidence \(e=(S,C)\) a vertex, partitioned by target
\(S\). Define the following bad sets, discarding sets containing two
vertices from the same target part.  After recording cell-collision pairs,
the other families may also be restricted to sets using distinct cells.

1. **Cell collision:** two incidences using the same cell.
2. **Empty position:** an inclusion-minimal family \(F\) whose cells contain
   \(p\) and for which
   \[
       \bar E_p\cap\bigcap_{(S,C)\in F}S=\varnothing.
   \]
3. **Middle-bit cover:** for \(b\in T_i\), put
   \(H_{i,b}=\{p\in I_i:b\in\bar E_p\}\). A bad set is an
   inclusion-minimal family of incidences with \(b\notin S\) whose cells
   cover \(H_{i,b}\).
4. **Protected-prepin-bit cover:** for a fixed prepin \((U,J)\) and
   \(b\in U\), put
   \(H_{\pi,b}=\{p\in J:b\in\bar E_p\}\).  A bad set is an
   inclusion-minimal family of residual incidences, all omitting \(b\),
   whose cells cover \(H_{\pi,b}\).
5. **Lower-bit cover:** for a distinguished incidence \(e_0=(S,C)\) and
   \(b\in S\), put \(H_{e_0,b}=\{p\in C:b\in\bar E_p\}\). A bad set is
   \(e_0\) together with an inclusion-minimal family of other incidences,
   all omitting \(b\), whose cells cover \(H_{e_0,b}\).

### Theorem 6.1 (conflict-transversal equivalence)

A choice of one incidence from every residual target part is a common-cap
matching, preserving the prepin bank, exactly when it contains none of these
bad sets.

Moreover:

- cell collisions have size two;
- every middle-bit bad set has size at most \(d+1\);
- every protected-prepin bad set has size at most \(d\);
- every lower-bit bad set has size at most \(d+1\);
- every empty-position bad set has size at most
  \[
     \min\!\left\{|\bar E_p|,\frac{d(d+1)}2\right\}\le r.
  \]

#### Proof

Cell collisions are precisely failure of injectivity. If a common-cap letter
is empty, its selected covering incidences contain a minimal empty-position
subfamily, and conversely.

A middle bit is absent exactly when the selected incidences omitting it cover
all envelope hosts. A minimal cover of a finite host set has a private host
for each member, so it has at most \(|H_{i,b}|\le d+1\) members.  A prepin
cell has at most \(d\) hosts.  The residual-lower statement is identical,
except that its distinguished incidence is added to a blocker cover of at
most \(|C|\le d\) hosts.

Finally, a minimal family of subsets of \(\bar E_p\) with empty intersection
has at most \(|\bar E_p|\) members: give each member a coordinate excluded by
it but retained by every other member. These coordinates are distinct. The
family is matching-compatible, so it uses distinct interval cells; at most
\(d(d+1)/2\) length-at-most-\(d\) integer intervals contain one position. The
five failure modes are exactly Theorem 5.1 together with the protected
prepin equalities. \(\square\)

## 7. Owner orientation removes the \(r\)-sized obstruction

Choose one coordinate \(o_p\in\bar E_p\) at every position. Retain only
incidences \((S,C)\) satisfying

\[
        o_p\in S\quad\text{for every }p\in C.
\tag{7.1}
\]

Every common cap formed from retained incidences contains \(o_p\) at
position \(p\). Empty-position bad sets disappear, and the remaining
conflict hypergraph has rank at most \(d+1\), independent of \(r\).

This is the point at which the construction can become uniform in \(k\): a
depth-\(d\) compiler needs bounded-depth conflict control rather than
rank-\(r\) intersection control.

### 7.2 Literal load bounds

Bounded rank is not bounded dependency.  The relevant constants must be
measured in the retained atlas.  Put

\[
 m=\min_S|D_S|,\qquad M=\max_S|D_S|,\qquad
 \lambda_C=|\{S:(S,C)\in D_S\}|,\qquad
 \lambda=\max_C\lambda_C.
\]

Let

\[
\begin{aligned}
A^-&=\max_{b,p}|\{(S,C):p\in C,\ b\notin S\}|,\\
A^+&=\max_{b,p}|\{(S,C):p\in C,\ b\in S\}|,
\end{aligned}
\tag{7.2}
\]

and let \(D=\max_i|I_i|\le d+1\).  For a candidate
\(v=(S,C)\), let \(\Pi(v)\) count protected-prepin requirements
\((\alpha,b)\) for which \(b\notin S\) and
\(C\cap H_{\alpha,b}\ne\varnothing\).

The same-cell event count is exactly

\[
        N_{\rm cell}=\sum_C\binom{\lambda_C}{2}.
\tag{7.3a}
\]

For a fixed bit-host set \(H\) of size \(h\), the number of minimal
size-\(j\) blocker covers is at most

\[
        (h)_j(A^-)^j\le(hA^-)^j.
\tag{7.3b}
\]

Assign each member of a minimal cover its distinct private host, then choose
a negative incidence through that host.

If \(B_j(v)\) is the number of size-\(j\) bad sets containing \(v\), then
the following literal worst-case bound holds after owner filtering:

\[
\begin{aligned}
B_j(v)\le{}&
 {\bf1}_{j=2}(\lambda_C-1)\\
&+(D+d-1)r(DA^-)^{j-1}\\
&+r(dA^-)^{j-1}\\
&+{\bf1}_{j\ge2}\,k d A^+(dA^-)^{j-2}\\
&+\Pi(v)(dA^-)^{j-1}.
\end{aligned}
\tag{7.3}
\]

Terms are omitted outside the rank of their conflict family.  The five lines
count same-cell pairs, middle covers, a lower incidence used as anchor, a
lower incidence used as blocker for another anchor, and prepin covers.
Without owner filtering, add \(d(rA^-)^{j-1}\) for empty-position events.

To prove (7.3), give every member of a minimal \(j\)-cover a distinct private
host.  A candidate cell meets at most \(D+d-1\) middle intervals.  There are
at most \(r\) relevant bits per middle or lower row, at most \(d\) positions
in a lower cell, and at most \(A^-\) negative or \(A^+\) positive candidates
through a fixed bit-position.  Multiplying these choices gives the displayed
terms.

Let

\[
 D_j(S)=|\{F:|F|=j,\ F\text{ uses target part }S\}|,\qquad
 \Gamma=\max_S\sum_jD_j(S).
\]

Then

\[
 D_j(S)\le M\max_vB_j(v),
\qquad
 \Delta(F)\le |F|\Gamma\le(d+1)\Gamma.
\tag{7.4}
\]

These are overcounts, but they are proof-safe.  Coarse Boolean information is
much weaker.  If

\[
 u=\max_C\left|\bigcup_{p\in C}\bar E_p\right|,
\qquad
 L_u=\sum_{q=1}^{r-1}\binom uq,
\]

then only

\[
 \lambda\le L_u,\qquad
 A^-,A^+\le\frac{d(d+1)}2L_u
\tag{7.5}
\]

follows without a carrier-specific dispersion theorem.  In the usual
\(u\le r\) setting, \(L_u\le2^r-1\).  Substitution into (7.3) is far too
large to imply an LLL asymptotically.

## 8. A concrete integral existence criterion

### Lemma 8.1 (owner-conflict local lemma)

After (7.1), suppose:

1. every residual target part has at least \(m\) incidences;
2. every bad set shares a target part with at most \(\Delta\) other bad sets;
3. every bad set has at least two vertices; and
4. \(e(\Delta+1)\le m^2\).

Then an integral common-cap matching exists.

#### Proof

Choose one incidence independently and uniformly from each target part. For
a bad set \(F\), the event that every member is selected has probability at
most \(m^{-|F|}\le m^{-2}\). Two such events are independent when their
target-part sets are disjoint, so dependency degree is at most \(\Delta\).
The symmetric Lovasz local lemma applies. One elementary parameter choice is
\(x=1/(\Delta+1)\) when \(\Delta\ge1\), since

\[
 x(1-x)^\Delta\ge\frac1{e(\Delta+1)}\ge m^{-2}.
\]

Thus a selection avoiding every bad set exists, and Theorem 6.1 makes it an
integral common-cap matching. \(\square\)

No fractional rounding or post hoc repair appears here.
When \(\Delta=0\), the bad events are mutually independent and the conclusion
follows directly; no \(x=1\) local-lemma witness is used.

### 8.2 Weighted lopsided criterion

The symmetric estimate can be replaced by its exact weighted form.  For a
bad set \(F\), let

\[
 p_F=\prod_{S\in\operatorname{parts}(F)}|D_S|^{-1},
\tag{8.2}
\]

and join two bad sets in the dependency graph when they share a target part.
If numbers \(x_F\in(0,1)\) satisfy

\[
 p_F\le x_F\prod_{G\sim F}(1-x_G)
\quad\text{for every }F,
\tag{8.3}
\]

then a common-cap matching exists.  This is the asymmetric local lemma
applied to the independent target-part variables.

A convenient, still rigorous scalar consequence is:

\[
 p_F\le\frac14,\qquad
 \sum_{G\sim F}p_G\le\frac{\log 2}{4}
\quad\text{for every }F.
\tag{8.4}
\]

Indeed, take \(x_F=2p_F\).  Since \(x_G\le1/2\),
\[
 \prod_{G\sim F}(1-x_G)
 \ge \exp\!\left(-2\sum_{G\sim F}x_G\right)
 \ge\frac12,
\]
which proves (8.3).

This is the correct place for a lopsided or nibble argument: one must bound
the **weighted conflict load**, not merely prove ordinary Hall expansion.

Using the part profiles from (7.4), a standard uniform arity-sensitive
sufficient test is the existence of \(0<a<1\) such that

\[
\frac1m\le
 a\prod_{j=2}^{d+1}(1-a^j)^{\max_S D_j(S)}.
\tag{8.5}
\]

Indeed, give every size-\(j\) bad event weight \(a^j\).  An event using
\(\ell\) target parts sees, with multiplicity as an upper bound, at most
\(\ell\max_S D_j(S)\) size-\(j\) events; taking the \(\ell\)-th root of the
asymmetric local-lemma inequality gives (8.5).

Unlike the symmetric test, (8.5) charges a size-\(j\) event at its natural
scale.  It still requires literal part profiles; bounded conflict rank alone
does not bound its product.

The sharper candidate-specific forms are proved in
`MATH_THEOREM_K_COMMON_CAP_ATOMIC_PRESSURE_AND_CUT_DUAL_20260731.md`.
There the lopsidependency graph joins only events prescribing different
candidates in a shared target part.  Its atomic opposition-capacity cut is

\[
 \sum_{v\in D_S}t_v
 \prod_{G\text{ opposing }v}
       \left(1-\prod_{u\in G}t_u\right)\ge1,
\]

and the complementary cluster-expansion cut is

\[
 \sum_{v\in D_S}b_v\ge
 1+\sum_{F:F\cap D_S\ne\varnothing}\prod_{v\in F}b_v.
\]

Both imply an integral common cap.  They are candidate-specific sufficient
conditions, not consequences of bounded rank.

### 8.3 Why generic LLL or nibble does not close the conjecture

For the coefficient-one scale,

\[
 W=\binom{k}{\lfloor k/2\rfloor}
   =\Theta(2^k/\sqrt{k}),\qquad d=\Theta(\sqrt{k}),
\]

and the lower-cell catalogue has order \(dW=\Theta(2^k)\) cells.  These
global counts do not control any of the quantities in (8.1) or (8.3):

- a target part may have degree one, even when the whole marginal graph has
  a perfect matching;
- owner restriction can reduce a large marginal part to zero;
- many candidate incidences can use one cell or one physical host;
- minimal blocker covers through different hosts can have large target-part
  codegree.

The failure is structural, not a weakness of the symmetric estimate.
Fix two middle hosts \(p,q\) for a bit \(b\), and a common owner bit \(o\).
Give target part \(A\) arbitrarily many individually legal cells which kill
\(b\) at \(p\) but retain \(o\), and target part \(B\) arbitrarily many
cells which kill \(b\) at \(q\) but retain \(o\).  Make all these cells
distinct.  Marginal Hall is perfect and both parts can have arbitrarily large
degree, but every choice of one \(A\)-cell and one \(B\)-cell deletes \(b\)
from the middle row.  The bad-event graph is complete bipartite between the
two parts; its bad-event union has probability one.  Owner orientation
prevents empty letters but does not repair this middle-bit obstruction.

The same example can be embedded with interval cells of bounded length by
adding private positions; the number of distinct cells through a host grows
with \(d\).  Therefore no theorem depending only on depth, part sizes,
ordinary Hall, or global density can establish (8.3).  A nibble likewise
needs a genuine low-codegree or negative-dependence estimate for the
carrier-specific conflict clutter.

There is an even simpler rank-two scaling obstruction.  Take \(n\) target
parts

\[
 V_i=\{(i,c):c\in[m]\},
\]

and make two vertices conflict exactly when they use the same cell \(c\).
Every part has size \(m\).  For \(n=m+1\) there is no transversal by the
pigeonhole principle, despite growing domains and rank-two conflicts.  For
\(n=m\), a transversal exists, but the canonical uniform LLL tests still
fail: a cell-collision event has ordinary dependency

\[
 2m^2-3m-1,
\]

so the symmetric product tends to \(2e\).  Here
\(D_2=m(m-1)\), and the largest right side of (8.5) is asymptotic to

\[
 \frac{e^{-1/2}}{\sqrt2\,m}<\frac1m.
\]

Thus failure of symmetric or uniform lopsided numerics is not itself an
obstruction certificate; tailored weights or deterministic structure may
still solve a particular atlas.

Unit propagation is also essential.  In the finite \(k=16\) calibration,
the pinned marginal graph has a large forced bank before the flexible core.
Thus its raw minimum part size is one, although the final integral compiler
exists.  Any asymptotic LLL attempt must first cap and audit the jointly
compatible forced bank, then prove (8.3) only on the residual flexible
system.

### 8.4 Exact finite cutwise criterion

When (8.3) is unavailable, Theorem 6.1 gives a proof-safe finite criterion.
Introduce \(y_e\in\{0,1\}\) and impose

\[
 \sum_{e\in D_S}y_e=1
 \quad(S\text{ residual}),\qquad
 \sum_{e:\operatorname{cell}(e)=C}y_e\le1
 \quad(C\in\mathcal C).
\tag{8.6}
\]

For every bad set \(F\), impose

\[
        \sum_{e\in F}y_e\le |F|-1.
\tag{8.7}
\]

The integral system (8.6)--(8.7) is feasible if and only if a common-cap
compiler exists for the fixed carrier, schedule, prepins, and catalogue.
Under an owner orientation, every separated inequality has width at most
\(d+1\).

There is an exact finite separation procedure.  Given an integral solution
of (8.6), form its maximal cap.  If a position is empty, shrink its selected
covering incidences to an inclusion-minimal empty intersection.  If a
middle, prepin, or selected-lower bit is missing, shrink the selected
blockers to a minimal cover of its host set.  Add (8.7).  Every cut is valid,
has the stated width, and excludes the current assignment.  Since (8.6) has
finitely many integral assignments, iteration terminates with either a
literal compiler or a finite infeasibility certificate.

This cutwise criterion is stronger than marginal Hall and is the exact
fallback when generic probabilistic hypotheses fail.

## 9. Inert/anchor Hall corollary

Call \(U\) **inert** if some cell \(J\) satisfies
\(\bigcup_{p\in J}\bar E_p=U\). Let \(\mathcal N\) be the non-inert targets,
and suppose every \(S\in\mathcal N\) has an individually exact singleton
candidate.

### Corollary 9.1 (anchor normal form)

Suppose there is an injection \(f:\mathcal N\to[0,L-1]\) using singleton
catalogue cells, with \((S,\{f(S)\})\) an individually exact incidence for
every \(S\). Put

\[
 A_p=
 \begin{cases}
 S,&p=f(S),\\
 \bar E_p,&p\notin f(\mathcal N).
 \end{cases}
\tag{9.1}
\]

If every middle and protected-prepin row remains exact and every inert \(U\)
has a cell \(J\)
which satisfies both

\[
 \bigcup_{p\in J}\bar E_p=U
 \quad\text{and}\quad
 \bigcup_{p\in J}A_p=U,
\tag{9.2}
\]

then \(A\) is a common-cap compiler.

#### Proof

Use \(\{f(S)\}\) for every non-inert target and choose the retained original
no-op cell from (9.2) for every inert target. Cells chosen for different
inert targets are distinct, since one original interval has only one union.
A surviving inert singleton cannot equal an anchor singleton with a
different value. Intersecting by the inert target does not alter a letter in
its chosen cell, because every \(\bar E_p\), and hence every \(A_p\), is
already a subset of that original cell union. Theorem 5.1 now applies.
\(\square\)

For an oriented Hall certificate, choose one proposed surviving cell \(J_U\)
for every inert \(U\), and designate a physical witness for every bit of
every middle row, every protected multi-cell prepin, and every bit of \(U\)
in \(J_U\). Let \(R_p\) be the bits designated at \(p\). Join
\(S\in\mathcal N\) to \(p\) when it is an exact singleton candidate,
\(R_p\subseteq S\), and \(\{p\}\) is not a chosen inert singleton. Hall's
condition in this graph implies Corollary 9.1.
Conversely, an anchor-normal-form compiler retaining one original no-op
occurrence per inert target admits such an orientation by choosing its
surviving witnesses. Thus existential oriented Hall is necessary and
sufficient **within this restricted normal form**, not for arbitrary
common-cap compilers.  Allowing an inert target to migrate to a new cell with
larger original envelope union destroys the converse.

## 10. Combined all-\(k\) theorem

### Theorem 10.1 (Pascal-reroot compiler)

Let \(k=2r\), let \(d\) be the desired overhead, and put
\(W=\binom{2r}{r}\). A universal word of length \(W+d\) exists if:

1. an odd-parent word satisfies Lemma 2.1;
2. two endpoint cuts satisfy (3.3);
3. the middle order has a length-\(W+d\) schedule satisfying
   (4.1)--(4.3);
4. every scarce prepin is capped by Lemma 4.1 and every non-singleton prepin
   equality remains in the protected-row family; and
5. the residual incidence system satisfies Theorem 5.1 directly, Lemma 8.1,
   or Corollary 9.1.

If the deadline lower bound gives \(\nu(2r)\ge W+d\), then
\(\nu(2r)=W+d\).

#### Proof

Lemma 2.1 supplies every middle target. Corollary 3.2 supplies every upper
target. Lemma 4.1, its retained protected equalities, and item 5 supply a
nonempty physical word realizing every lower and middle target. The
no-chain-break condition transfers each consecutive upper witness to a
physical interval. The word is universal and has length \(W+d\); combine
with the lower bound. \(\square\)

For an odd target dimension, Sections 3--9 apply verbatim once an
upper-complete middle carrier is supplied; only the even Pascal-raising
Lemma 2.1 is omitted.

## 11. Calibration and the genuine all-\(k\) gate

For \(k=16\), \(r=8\), \(d=3\):

- the parent has exception \(c=6390\), \(P_c=\mathtt{0x13c8}\);
- the endpoint reroots are prefix \([0,6388]\) and suffix
  \([12826,12869]\);
- starts \(12870,12871,12872\) and deadlines \(0,1,6388\) are omitted;
- \(\mathtt{0x8000}\) is prepinned at position \(6389\);
- the decoded common-cap word has length \(12873\), SHA-256
  890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe,
  and covers all \(65535\) nonempty masks.

Together with the deadline lower bound, this proves
\(\nu(16)=12873\). The certificate verifies Theorem 10.1 through the direct
Theorem 5.1 alternative. It does **not** prove that (7.1)--(8.1), the
inert/anchor normal form, or the same reroots recur for all \(r\).

The reusable all-\(k\) gate is:

> construct the one-defect Pascal parent and two-ray absorber, then choose
> owners so that the depth-\(d\) conflict hypergraph has an integral
> transversal, by bounded dependency, oriented Hall, or a stronger
> carrier-specific expansion theorem.

This separates Pascal middle ownership, endpoint upper absorption, and joint
lower compilation.

## 12. Authenticated calibration

- MATH_CERTIFICATE_K16_OPTIMAL_12873_20260731.md
- scratch/k16_optimal_12873_20260731.word, SHA-256
  890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe
- scratch/k16_c7be_commonq_chain_independent_20260731.audit.json
- scratch/k16_optimal_12873_independent_local_v2_20260731.audit.json,
  payload 23895704144b7257e1c514746310213d5a1cef624cbedc59357cf20ffba040a7
- MATH_AUDIT_ABSTRACT_ONE_DEFECT_PASCAL_REROOT_PREPIN_20260731.md,
  SHA-256 f6f2c1e212fa74c01b310874749d672cea953724860e71911019d42f7d7d4cc0
- MATH_AUDIT_CONFLICT_HYPERGRAPH_AND_LLL_SCALING_20260731.md,
  SHA-256 964bf11aed55bd2b6789902d91c116f0c482b5a2655bd5b6eca36f3abd8e77b4
- MATH_THEOREM_K_COMMON_CAP_ATOMIC_PRESSURE_AND_CUT_DUAL_20260731.md,
  with its independent audit
  MATH_AUDIT_K_COMMON_CAP_ATOMIC_PRESSURE_AND_CUT_DUAL_20260731.md
- MATH_THEOREM_K16_C7BE_INERT_SINGLETON_ORIENTED_ANCHOR_NORMAL_FORM_20260731.md,
  an independently audited restricted normal form, not an all-\(k\)
  existence claim

These artifacts calibrate the theorem but are not used to infer its uniform
hypotheses.
