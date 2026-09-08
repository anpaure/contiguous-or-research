# The monotone-deadline run staircase

## 1. Setting

Let

\[
T_0,T_1,\ldots,T_{W-1}\subseteq[k]
\]

be a proposed middle carrier. Fix an excess \(d\), put \(L=W+d\), take
the physical starts to be

\[
s_i=i\qquad(0\le i<W),
\]

and take the physical deadlines \(e_i\) to be the increasing enumeration of

\[
[0,L-1]\setminus Y,\qquad |Y|=d.
\]

Thus the omitted starts are the final \(d\) positions. Write

\[
h_i=e_i-i.
\]

The sequence \(h_i\) is nondecreasing and takes values in
\(\{0,1,\ldots,d\}\). The maximal middle envelope is

\[
E_p=\bigcap_{i:i\le p\le e_i}T_i,
\]

where an empty intersection is the full coordinate set.

This note gives an exact criterion for

\[
\bigvee_{p=i}^{e_i}E_p=T_i\qquad(0\le i<W).
\tag{1.1}
\]

It also couples that criterion to the exact number of available lower
cells. No probabilistic or solver assumption is used.

## 2. Exact run criterion

For one coordinate \(x\), consider a maximal run

\[
[a,b]=\{i:x\in T_i\}.
\]

Put \(e_{-1}=-1\).

### Theorem 2.1 (run--deadline equivalence)

The maximal envelope has the row ORs in (1.1), allowing an empty envelope
letter at a position, if and only if
every **interior** coordinate run \([a,b]\), meaning
\(0<a\le b<W-1\), satisfies

\[
b\ge e_{a-1}+1.
\tag{2.1}
\]

Equivalently, every interior run has length

\[
b-a+1\ge h_{a-1}+1.
\tag{2.2}
\]

Runs beginning at \(0\) or ending at \(W-1\) impose no condition.  This is
not a claim that there are two literal physical tails: on the left the
condition disappears because there is no preceding absent row, whereas on
the right the final physical tail is available when a witness must lie past
the last carrier start.

#### Proof

Fix an interior run \([a,b]\). A physical position \(p\) may carry \(x\)
precisely when every row interval containing \(p\) has index in \([a,b]\).
Since the starts and deadlines are increasing, the row indices containing
\(p\) form

\[
[\alpha(p),p]\cap[0,W-1],
\qquad
\alpha(p)=\min\{j:e_j\ge p\}.
\]

For \(i\in[a,b]\), choose

\[
p_i=\max\{i,e_{a-1}+1\}.
\]

Strict increase of the deadlines gives \(p_i\le e_i\). Condition (2.1)
also gives \(p_i\le b\), while \(e_{a-1}<p_i\) gives
\(\alpha(p_i)\ge a\). Therefore every row containing \(p_i\) lies inside
\([a,b]\), so \(x\in E_{p_i}\), and row \(i\) recovers \(x\).

Conversely suppose \(e_{a-1}\ge b\). To recover \(x\) in row \(a\), a
position \(p\in[a,e_a]\) would be needed. If \(p\le b\), the preceding
row \(a-1\) also contains \(p\), so \(x\notin E_p\). If \(p>b\), then
\(p\ge b+1\) and, because \(p\le e_a\le e_{b+1}\), the following absent
row \(b+1\) contains \(p\), again excluding \(x\). Thus (2.1) is necessary.

At the left boundary there is no preceding absent row. At the right
boundary, \(p=e_{a-1}+1\) is available beyond the final carrier start when
needed and no following absent row exists. The same construction therefore
recovers boundary runs unconditionally. Applying the argument to every
coordinate proves the theorem. \(\square\)

The original word problem forbids empty letters. That condition is separate
and has the following exact form.

### Lemma 2.2 (nonempty-envelope condition)

For a physical position \(p\), let

\[
B_p=\{i:i\le p\le e_i\}.
\]

Then

\[
E_p\ne\varnothing
\quad\Longleftrightarrow\quad
\bigcap_{i\in B_p}T_i\ne\varnothing.
\tag{2.3}
\]

Every nonempty \(B_p\) is a consecutive block of at most \(d+1\) carrier
rows. Consequently it is enough that every consecutive block of at most
\(d+1\) carrier rows have nonempty intersection. In particular, this holds
for a Johnson path of rank \(r>d\): across \(s-1\le d\) Johnson steps, at
most \(s-1\) elements of the first row can be deleted, leaving intersection
size at least \(r-(s-1)>0\).

#### Proof

Equation (2.3) is the definition of \(E_p\). Monotonicity of starts and
deadlines makes \(B_p\) consecutive, and \(i\le p\le e_i\le i+d\) bounds
its size by \(d+1\). The Johnson-path estimate is the deletion union bound.
\(\square\)

## 3. The \(d\) threshold statistics

For \(1\le j\le d\), define the height threshold

\[
\tau_j=\min\{i:h_i\ge j\},
\]

with \(\tau_j=W\) if height \(j\) is never reached. Then

\[
0\le\tau_1\le\tau_2\le\cdots\le\tau_d\le W.
\]

For the carrier, define its short-run frontier

\[
\rho_j=\max\bigl(
 \{a:\text{an interior coordinate run starts at }a
       \text{ and has length at most }j\}\cup\{0\}\bigr).
\tag{3.1}
\]

The frontiers are also nondecreasing.

### Corollary 3.1 (staircase criterion)

The maximal envelope realizes \(T\) if and only if

\[
\tau_j\ge\rho_j\qquad(1\le j\le d).
\tag{3.2}
\]

#### Proof

An interior run of length \(\ell\le d\) beginning at \(a\) satisfies (2.2)
exactly when \(h_{a-1}<\ell\), equivalently \(a\le\tau_\ell\). Longer runs
are automatic because \(h_i\le d\). Taking maxima gives (3.2).
\(\square\)

The correspondence is a bijection: every nondecreasing threshold vector
occurs, and its unique omitted deadlines are

\[
y_j=\tau_j+j-1\qquad(1\le j\le d).
\tag{3.3}
\]

Indeed these are strictly increasing members of \([0,L-1]\).  Conversely,
if \(y_j\) is the \(j\)-th omitted deadline, then the first retained deadline
after \(y_j\) has retained-row index \(y_j-(j-1)\), so height \(j\) begins at
\(\tau_j=y_j-j+1\).  This proves both existence and uniqueness.

## 4. Exact capacity identity

The number of proper-prefix cells below the selected middle rows is

\[
\mathcal A=\sum_{i=0}^{W-1}h_i.
\]

The threshold decomposition gives

\[
\sum_i(d-h_i)=\sum_{j=1}^d\tau_j,
\qquad
\mathcal A=dW-\sum_{j=1}^d\tau_j.
\tag{4.1}
\]

The boundary staircase contributes the additional
\(\binom{d+1}{2}\) short cells from the final \(d\) physical starts. If

\[
\Lambda=\sum_{s=1}^{r-1}\binom{k}{s}
\]

is the number of required nonempty lower targets and

\[
\Delta=dW+\binom{d+1}{2}-\Lambda,
\tag{4.2}
\]

then the catalogue has at least \(\Lambda\) cells exactly when

\[
\sum_{j=1}^d\tau_j\le\Delta.
\tag{4.3}
\]

Combining Corollary 3.1 with (4.3) gives the promised scalar criterion.

### Theorem 4.1 (minimal staircase budget)

Among all canonical monotone-deadline schedules, the minimum lost capacity
compatible with the exact row-OR conditions of a carrier \(T\) is

\[
\boxed{\mathsf R_d(T)=\sum_{j=1}^d\rho_j}.
\tag{4.4}
\]

Consequently, within the canonical tail-start/monotone-deadline class, a
carrier admits a row-exact maximal middle envelope and enough physical lower
cells if and only if

\[
\boxed{\mathsf R_d(T)\le\Delta}.
\tag{4.5}
\]

The canonical witnessing schedule takes \(\tau_j=\rho_j\) and
\(y_j=\rho_j+j-1\).

For this schedule to be a legal nonempty word, Lemma 2.2 must additionally
hold. It is automatic under the \(d\)-local intersection condition, hence
for Johnson carriers of rank \(r>d\). This theorem concerns middle
realization and scalar lower capacity. It does not assert the Hall/common-cap
assignment of distinct lower targets; that is the separate compiler gate.

## 5. Checks and implications

For the authenticated \(k=16\) carrier, the retained schedule has

\[
Y=\{0,1,6388\},\qquad
(\tau_1,\tau_2,\tau_3)=(0,0,6386),
\]

and hence

\[
\mathcal A=3W-6386=32224,
\]

exactly the certificate's selected area. The endpoint reroot is therefore
read as a relocation of every interior length-three run start before the
third threshold. The carrier's *minimal* frontier is

\[
(\rho_1,\rho_2,\rho_3)=(0,0,6384).
\]

The retained schedule deliberately spends two additional units of scalar
capacity; those units support its chosen singleton pin and common-cap
compiler. Thus the minimal staircase is a feasibility baseline, not a claim
that the compiler-optimal schedule always takes \(\tau=\rho\).

For reference, here \(W=12870\), \(\Lambda=26332\), and
\(\Delta=12284\).  The retained schedule has \(32224\) proper-prefix cells
and \(32230\) physical lower cells after adding the six boundary cells.  A
direct maximal-envelope replay has no empty letter for this particular
carrier and schedule; this is an instance-specific check, not a consequence
of the scalar budget alone.

For the \(k=16\to17\) Pascal-shadow experiment, upper completeness of the
selected old-rank-nine shore is not the only condition. Its short-run
frontier must also obey (4.5), possibly after bounded rerooting. This gives
an exact and very cheap rejection test for every candidate carrier and tells
the search which defects matter: not the number of short runs, but the last
start of runs of each length \(1,\ldots,d\).

The optimized upper-73 sector chronology, with SHA-256
ea10337264c7998d227cf4c8ef5d5df463d5fb4efd9c29c7a1e0171d7b4897a4,
audited on 2026-07-31 has

\[
(\rho_1,\rho_2,\rho_3)=(11440,11440,17824),
\qquad
\mathsf R_3=40704>7401=\Delta_{17}.
\]

The first-occurrence raw chronology, SHA-256
1f320529b533d8ec744ac6c2845c60f4507ed69e23d0fdeda46319ba8be94776,
has the same frontier and the same decisive bit-7 singleton run.

Therefore that unrerooted two-shore carrier is rigorously incapable of an
optimal canonical schedule even if its remaining upper holes are repaired.
Thus the canonical final-start-hole \(k=17\) lane must jointly rethread
residence and upper coverage; an upper-only occurrence selector is not
enough **in that lane**.  This calculation does not rule out a noncanonical
schedule with internal omitted starts, because Theorem 4.1 fixes
\(s_i=i\).
