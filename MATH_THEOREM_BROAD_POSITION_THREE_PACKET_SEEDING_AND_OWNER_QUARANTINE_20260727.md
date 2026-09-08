# Broad position-three support can be seeded with polynomial owner quarantine

Date: 2026-07-27

Method: pure mathematics only.  No computation, finite search, solver,
web input, or random-like nibble is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad d=m-3H+1=M-4H+1,
\tag{0.1}
\]

\[
 N=\binom{2m}{M},\qquad W=\binom{2m}{m},
\tag{0.2}
\]

and assume

\[
 H=o(m),\qquad H\ge3,\qquad M\ge18H-10.
\tag{0.3}
\]

The last inequality is only needed for the twelve-top packet.  The
three-top conclusions need the weaker hypotheses in the three-top
recharge theorem.

The position--label histogram cut says that a coefficient-one initial
state capable of supplying all but \(o(W)\) of the certified rectangle
directions must have

\[
             |S_3|=2m-o(m).
\tag{0.4}
\]

This note proves that (0.4) is not a second coefficient-scale packing
problem.  It can be forced by a deterministic polynomial-size seed
bank.

### Theorem A (simultaneous broad packet seed bank)

For all sufficiently large \(m\), there is a resource-disjoint bank
consisting of

* one literal three-top source packet \(P_c^{(3)}\) for every
  \(c\in[n]\); and
* one literal twelve-top source packet \(P_c^{(12)}\) for every
  \(c\in[n]\),

such that a designated source row of each \(P_c^{(s)}\) has label
\(c\) in rooted position three.  The complete bank uses exactly

\[
                         15n
\tag{0.5}
\]

distinct tops and exactly

\[
                         15nd
\tag{0.6}
\]

distinct middle owners.  Thus its union is coefficient one and has

\[
                         S_3=[n].
\tag{0.7}
\]

Every subcollection of the bank can be switched, in any order, from
source shore to target shore.  Every intermediate state remains
coefficient one and preserves the complete protected trace ledger.

### Theorem B (broad-support completion with quarantine)

Let \({\cal T}\) be any partial coefficient-one retained-path table:
it has at most one row on each rank-\(M\) top, every row has \(d\)
distinct middle owners, and different rows have disjoint owner decks.
There is a deterministic modification \({\cal T}'\) which contains the
whole bank of Theorem A, satisfies \(S_3({\cal T}')=[n]\), and is still
coefficient one.

If

\[
 \delta=N-|{\cal T}|,\qquad
 \varepsilon=W-|\operatorname{mid}{\cal T}|
\tag{0.8}
\]

are the top and owner defects, then

\[
 \delta'\le \delta+15n(1+d),
 \qquad
 \varepsilon'\le \varepsilon+15nd(1+d).
\tag{0.9}
\]

If \({\cal T}\) initially has one row on every top, the sharper bounds
are

\[
 \delta'\le15nd=O(m^2),
\tag{0.10}
\]

and

\[
 \varepsilon'=W-dN+d\delta'
 \le W-dN+15nd^2.
\tag{0.11}
\]

In the calibrated regime \(W/N=M+O(H)\), this is

\[
                         \varepsilon'=o(W).
\tag{0.12}
\]

Thus broad position-three support, literal three-top compatibility,
literal twelve-top compatibility, and exact middle squarefreeness can
be obtained with only \(O(m^3)=o(W)\) quarantine cost.

### Exact boundary

The theorem does **not** construct the underlying near-spanning
coefficient-one table.  It proves the following sharper reduction.

* Once any coefficient-one near-factor is available, histogram breadth
  can be added at \(o(W)\) cost.
* If one insists on one retained path on every top with no quarantine,
  the exact condition is that the seed owner support avoid every
  nonseed row.  Producing such a bank is precisely an owner-aware source
  installation problem, not a position-histogram problem.
* The polynomial seed bank is not the positive-density recurrent packet
  circulation needed for the final compiler.

Accordingly there is no stronger \(\Omega(W)\) obstruction coming from
the demand \(|S_3|=2m-o(m)\) itself.  The surviving obstruction is the
old middle-owner near-factor/source-allocation gate.

## 1. Retained paths and defects

Let \(p=(p_1,\ldots,p_M)\) be a rooted cyclic order on a rank-\(M\)
top \(U\).  Its retained middle deck is

\[
 {\cal O}(U,p)
 =\left\{
 U\setminus\{p_s,p_{s+1},\ldots,p_{s+H-1}\}:
 1\le s\le d
 \right\}.
\tag{1.1}
\]

The chosen cut makes (1.1) linear: none of the displayed intervals
wraps around the root.  An injective word has \(d\) distinct owners.

A **partial coefficient-one table** is a set of such rows on distinct
tops for which the decks (1.1) are pairwise disjoint.  Its position-three
support is

\[
 S_3({\cal T})
 =\{c\in[n]:p_U(3)=c\text{ for some row }(U,p_U)\in{\cal T}\}.
\tag{1.2}
\]

Every table with \(r\) rows has exactly \(dr\) covered middle owners.
Consequently its two defects obey the identity

\[
                         \varepsilon=W-d(N-\delta).
\tag{1.3}
\]

This elementary identity is useful below: a polynomial top quarantine
has only polynomial owner cost.

## 2. The exact singleton owner ledger does not force position three

It is tempting to hope that coefficient one already forces almost every
label to appear in position three.  The exact singleton ledger shows
why this does not follow.

For \(1\le t\le M\), put

\[
 a_t
 =\#\{s\in[d]:s\le t\le s+H-1\}
 =\max\bigl(0,\min(d,t)-\max(1,t-H+1)+1\bigr).
\tag{2.1}
\]

Thus a label in position \(t\) is deleted from exactly \(a_t\) of the
\(d\) owners in its row and belongs to the other \(d-a_t\).

Suppose for this section that \({\cal T}\) has one row on every top.
Write

\[
 H_{t,c}=\#\{U:p_U(t)=c\},
\qquad
 q_c=\#\{X\notin\operatorname{mid}{\cal T}:c\in X\}.
\tag{2.2}
\]

Let

\[
                         R=\binom{n-1}{M-1}=\frac MnN.
\tag{2.3}
\]

### Proposition 2.1 (exact singleton equations)

For every label \(c\),

\[
 \sum_{t=1}^M(d-a_t)H_{t,c}=\frac W2-q_c,
\tag{2.4}
\]

or equivalently

\[
 \boxed{
 \sum_{t=1}^Ma_tH_{t,c}=dR-\frac W2+q_c.}
\tag{2.5}
\]

Moreover

\[
                         \sum_{c=1}^n q_c=m(W-dN).
\tag{2.6}
\]

#### Proof

Exactly \(R\) tops contain \(c\), so
\(\sum_tH_{t,c}=R\).  A row with \(c\) in position \(t\) contributes
\(d-a_t\) covered owners containing \(c\).  Since coefficient one
makes these owners distinct, their total is the number \(W/2\) of
middle sets containing \(c\), minus the \(q_c\) uncovered ones.  This
proves (2.4), and subtraction from \(dR\) gives (2.5).  Finally every
uncovered middle set contains exactly \(m\) labels, proving (2.6).
\(\square\)

The equations do not isolate position three.  Indeed

\[
                         a_3=3
                         =a_{d+H-3}
\tag{2.7}

for the present range of parameters.  Thus even the complete family of
singleton owner equations gives the same coefficient to position three
and to a remote position.  Coefficient one by itself supplies no
lower bound on \(H_{3,c}\).  The breadth requirement is a genuine
initialization condition, but Theorems A and B show that it is a cheap
one at the \(W\)-scale.

## 3. A deterministic orbit-seeding lemma

We isolate the only counting fact needed for the construction.

Consider one fixed role-labelled packet template.  Suppose every
labelled copy has

\[
 s\text{ distinct tops},\qquad sd\text{ distinct middle owners},
\tag{3.1}
\]

and its labels are obtained by injecting a fixed set of roles into
\([n]\).  Fix one distinguished role \(\rho\) which occupies rooted
position three in one source row.  Let \(\Omega_c\) be the copies in
which \(\rho\) receives label \(c\).

### Lemma 3.1 (conditional resource incidences)

If a copy is counted uniformly in the full role-injection orbit, then
for every fixed top \(U\) and owner \(X\),

\[
 \Pr[U\text{ is used}]=\frac{s}{N},
 \qquad
 \Pr[X\text{ is used}]=\frac{sd}{W}.
\tag{3.2}
\]

Conditioning on \(\rho=c\) gives the bounds

\[
 \Pr[U\text{ is used}\mid\rho=c]\le\frac{ns}{N},
 \qquad
 \Pr[X\text{ is used}\mid\rho=c]\le\frac{nsd}{W}.
\tag{3.3}
\]

#### Proof

The symmetric group on \([n]\) is transitive on rank-\(M\) tops and
on rank-\(m\) owners.  Every copy has exactly the resource counts in
(3.1), so double counting copy--resource incidences gives (3.2).
The distinguished role is uniform on \([n]\), hence
\(\Pr[\rho=c]=1/n\).  For either resource event \(E\),

\[
 \Pr[E\mid\rho=c]
 \le\frac{\Pr[E]}{\Pr[\rho=c]}=n\Pr[E],
\]

which is (3.3). \(\square\)

### Lemma 3.2 (polynomial prescribed-colour packing)

Suppose \(s\le12\).  Given any list of at most \(2n\) requests, each
request specifying a packet type of the above form and a desired label
\(c\) for its distinguished position-three role, the requests admit
pairwise top-disjoint and owner-disjoint copies for all sufficiently
large \(m\).

#### Proof

Choose the copies greedily.  After \(j\) choices, at most \(12j\) tops
and \(12dj\) owners are forbidden.  Lemma 3.1 and the union bound show
that the proportion of the next conditional orbit meeting a forbidden
resource is at most

\[
 (12j)\frac{12n}{N}
 +(12dj)\frac{12nd}{W}
 =\frac{144nj}{N}+\frac{144nd^2j}{W}.
\tag{3.4}
\]

For \(j\le2n\), the right side is

\[
 O\left(\frac{m^2}{N}+\frac{m^4}{W}\right)=o(1),
\tag{3.5}
\]

because \(M=m+o(m)\), so both \(N\) and \(W\) are exponential in
\(m\).  In particular (3.4) is less than one for all sufficiently
large \(m\); at least one legal next copy exists.  This is a finite
averaging argument and a deterministic greedy choice, not a nibble.
\(\square\)

## 4. Construction of the broad source bank

The three-top packet has \(s=3\), uses \(M+1\) distinct label roles,
and has a squarefree source support of size \(3d\).  Its source table
at the two active positions is

\[
\begin{array}{c|cc}
 &3&b\\ \hline
 C+\{x,y\}&x&y\\
 C+\{x,a\}&a&x\\
 C+\{a,y\}&y&a .
\end{array}
\tag{4.1}
\]

Thus the role \(x\) in the first row is an eligible distinguished
position-three role.

The twelve-top packet has \(s=12\), uses a common \((M-2)\)-core and
six outside labels, hence \(M+4\) distinct roles, and has a squarefree
source support of size \(12d\).  Fix any one role occupying position
three in one of its twelve source rows.  Relabelling all roles by an
injection preserves the complete word, palette, squarefreeness, and
trace identities of the template.

Apply Lemma 3.2 to the \(2n\) requests

\[
 (3,c),\ (12,c),\qquad c\in[n].
\tag{4.2}
\]

This gives the claimed pairwise resource-disjoint copies.  Their top
and owner counts are

\[
 n(3+12)=15n,
 \qquad
 n(3d+12d)=15nd.
\tag{4.3}
\]

Every label \(c\) occurs in position three in a designated row, proving
\(S_3=[n]\).  Both local packet theorems say that source and target
shores have the same squarefree owner support and the same complete
protected aggregate trace.  Resource-disjoint packets do not affect
one another.  They may therefore be switched in an arbitrary order,
proving Theorem A.

There is deliberate redundancy in (4.2).  If only the three-top or
only the twelve-top library is needed, retain the corresponding \(n\)
requests and replace the constants \(15\) by \(3\) or \(12\).

## 5. Overwriting an arbitrary coefficient-one table

Let \({\cal B}\) be the bank of Theorem A, and write

\[
 {\cal U}({\cal B})=\text{its }15n\text{ tops},
 \qquad
 {\cal O}({\cal B})=\text{its }15nd\text{ owners}.
\tag{5.1}
\]

Let \({\cal D}\subseteq{\cal T}\) be the set of old rows which
conflict with the bank: a row lies in \({\cal D}\) if either its top
belongs to \({\cal U}({\cal B})\), or its owner deck meets
\({\cal O}({\cal B})\).

### Lemma 5.1 (exact collision charge)

\[
                         |{\cal D}|\le15n(1+d).
\tag{5.2}
\]

#### Proof

Charge a conflicting row to one witnessing bank top or bank owner.
Because \({\cal T}\) is coefficient one, one top or one owner can
witness at most one old row.  There are exactly \(15n+15nd\) possible
witnesses. \(\square\)

Delete \({\cal D}\) and insert all source rows of \({\cal B}\):

\[
             {\cal T}'=({\cal T}\setminus{\cal D})
                         \mathbin{\dot\cup}{\cal S}^-({\cal B}).
\tag{5.3}
\]

By definition no surviving old row meets a bank resource.  The bank is
internally resource-disjoint.  Hence (5.3) is coefficient one, and
Theorem A gives \(S_3({\cal T}')=[n]\).

The row and owner counts are exact:

\[
 |{\cal T}'|=|{\cal T}|-|{\cal D}|+15n,
\tag{5.4}
\]

\[
 |\operatorname{mid}{\cal T}'|
 =|\operatorname{mid}{\cal T}|-d|{\cal D}|+15nd.
\tag{5.5}
\]

Thus

\[
 \delta'=\delta+|{\cal D}|-15n,
 \qquad
 \varepsilon'=\varepsilon+d|{\cal D}|-15nd.
\tag{5.6}
\]

Equations (0.9) follow from (5.2).  If \(\delta=0\), then
(1.3) applied to \({\cal T}'\) gives

\[
 \varepsilon'=W-d(N-\delta')=W-dN+d\delta'.
\tag{5.7}
\]

Also (5.2) and (5.6) give

\[
 \delta'\le15nd,
 \qquad
 \varepsilon'\le W-dN+15nd^2.
\tag{5.8}
\]

Under \(W/N=M+O(H)\),

\[
 W-dN=(W/N-d)N=O(HN)=o(W),
\tag{5.9}
\]

while \(15nd^2=O(m^3)=o(W)\).  This proves Theorem B.

Notice that every collision has been paid for literally.  No equality
of expected owner loads, quotient flow, or profile count is being used.

## 6. The exact zero-quarantine installability condition

Suppose now that \({\cal T}\) has one row on every top.  Let
\({\cal T}[{\cal U}({\cal B})]\) be its \(15n\) rows on the bank tops.

### Proposition 6.1 (exact owner/installability criterion)

Replacing precisely those \(15n\) old rows by the bank source shore
gives another full coefficient-one table if and only if

\[
 {\cal O}({\cal B})\cap
 \operatorname{mid}\bigl(
 {\cal T}\setminus{\cal T}[{\cal U}({\cal B})]
 \bigr)=\varnothing.
\tag{6.1}
\]

Equivalently, the collision set in Section 5 has size exactly \(15n\):

\[
                         |{\cal D}|=15n.
\tag{6.2}
\]

#### Proof

All old rows on bank tops must be removed because a table has at most
one row per top.  Their owner decks then become free.  The inserted bank
is internally coefficient one.  Therefore its only possible collision
is with an unchanged row on a nonbank top, which is excluded exactly by
(6.1).  Since every bank top has one old row, (6.1) is also equivalent
to saying that no additional row enters \({\cal D}\), namely (6.2).
\(\square\)

Condition (6.1) is the raw physical source-allocation gate.  It is not
implied by broad histogram support, by the symmetric packet orbit, or
by a top-only packing of twelve-top carriers.  Conversely, once (6.1)
holds, there is no further owner, collar, or chronology condition for
installing this seed bank: all packets are literal and resource-disjoint.

If (6.1) fails, Theorem B deletes the additional colliding rows and
pays for them by (5.8).  Restoring a row on every deleted nonbank top
without losing a bank row asks for new retained paths whose complete
owner decks lie in the residual owner holes.  That is exactly a
residual promotion-path factor problem.  It is not a consequence of a
Hall inequality on individual owner incidences because the \(d\)
owners of one row must be taken as one consecutive Johnson path.

## 7. Consequence for the deterministic constant-one gate

The position-histogram capacity theorem required

\[
                         |S_3|\ge2m-O(H).
\tag{7.1}
\]

Theorems A and B give the stronger \(|S_3|=2m\) while losing only
\(O(m^2)\) rows and \(O(m^3)\) owner occurrences.  Both losses are
\(o(W)\).  Thus the deterministic gate separates as follows.

### Proved

1. The exact singleton owner ledger does not automatically force broad
   position-three support.
2. Every coordinate can be installed as a literal position-three token
   in both the three-top and twelve-top source libraries.
3. All \(4m\) prescribed packet copies can be chosen simultaneously
   with no top or middle-owner collision.
4. Any pre-existing coefficient-one near-factor can be converted to a
   broad, packet-compatible coefficient-one partial table with
   \(o(W)\) quarantine.
5. The exact condition for doing the same replacement with zero
   quarantine is (6.1).

### Not proved

1. An unconditional one-row-per-top coefficient-one retained-path
   factor at the calibrated height.
2. A bank satisfying (6.1) relative to an arbitrary prescribed full
   table.
3. A positive-density owner-disjoint packing of three-top or twelve-top
   source packets.
4. The recurrent state flow exposing \(W-o(W)\) distinct rectangle
   directions.

Therefore the broad-support specification is met at the coefficient-one
\(W+o(W)\) level, but not by an exact unquarantined all-top factor.
Any claimed full solution must still prove the owner-aware near-factor
or an equivalent residual completion theorem; position-histogram
breadth is no longer an independent asymptotic obstruction.
