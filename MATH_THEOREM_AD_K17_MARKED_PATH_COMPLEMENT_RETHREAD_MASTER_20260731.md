# The `K17` marked-path complement-rethread master

Date: 2026-07-31  
Status: exact finite reduction and complete column census; simultaneous upper
service, complement residence, deep shadows, connectivity, and one common
compiler are not yet solved

## 1. Result

The OPTIMAL28 residual-`U` pairing face is upper-`q1` impossible: `218`
rank-ten colours have no provider while all macro and packet objects are kept
intact.  At the individual-column level, the obstruction does **not by
itself** force the residence-clean marked path to change.

Freeze instead only

* the `4108` marked owners and their `4107` internal lower-colour edges; and
* the two cross edges joining that path to its complement.

Then rethread the `20202` complementary owners arbitrarily, subject to using
each of the remaining `20201` lower colours once.  This produces an exact
signed master with `545721` off-source edge columns.  Every one of the `218`
fixed-pairing upper holes has between `10` and `45` marked-preserving columns;
indeed every one of the current carrier's `1900` upper holes has between `10`
and `45`.  Thus there is no single-target column-domain obstruction after the
complement object interiors are released.  This does not say that any one of
those columns extends to a balanced connected global selection.

The exact remaining gate is simultaneous: choose the columns so that owner
degrees balance, the complement is one path between the two boundary owners,
all upper rows survive, and the resulting chronology also satisfies
residence, deeper shadows, and the common compiler.  Sections 3--5 give an
exact zero-proxy formulation of the first three conditions.

## 2. Frozen path and complementary colour bank

Let `W` be the authenticated lower-rainbow Hamilton cycle on all

\[
                         {17\choose9}=24310
\]

rank-nine owners.  Its edge colour is the rank-eight intersection.  Let
\(M\) be the marked owner set and \(C=V(W)\setminus M\).  Literal replay gives

\[
                         |M|=4108,\qquad |C|=20202.  \tag{2.1}
\]

The edge partition is

\[
 E(W)=E_{MM}\mathbin{\dot\cup}E_{MC}\mathbin{\dot\cup}E_{CC},
 \qquad (|E_{MM}|,|E_{MC}|,|E_{CC}|)=(4107,2,20201). \tag{2.2}
\]

Hence \(W[M]\) and \(W[C]\) are paths, and the two cross edges join their
corresponding endpoints.  Freeze \(E_{MM}\cup E_{MC}\).  Let

\[
 \Gamma=\{u\cap v:\{u,v\}\in E_{CC}\};qquad |\Gamma|=20201. \tag{2.3}
\]

For each \(c\in\Gamma\), write \(e_c^0=\{a_c,b_c\}\) for its current
complement edge and define its complete complement edge bank

\[
 \mathcal E_c=
 \bigl\{\{u,v\}:u,v\in C,\ u\ne v,\ u\cap v=c\bigr\}.          \tag{2.4}
\]

Because two distinct rank-nine supersets of a rank-eight set intersect in
that set, every member of \(\mathcal E_c\) is a legal Johnson edge of lower
colour \(c\).  Conversely every complement Johnson edge of colour \(c\)
appears in (2.4).  Thus this is the complete, not width-restricted,
marked-preserving rethread catalogue.

The number \(q_c\) of complement rank-nine supersets of \(c\) has profile

\[
 q_c:\quad3^{15},4^{129},5^{454},6^{1601},7^{3836},
              8^{6748},9^{7418}.                     \tag{2.5}
\]

Therefore the exact number of alternatives to the current edge is

\[
 \sum_{c\in\Gamma}\left({q_c\choose2}-1\right)=545721,         \tag{2.6}
\]

and the catalogue including the `20201` keep choices has `565922` columns.

## 3. Smallest signed degree master

For every \(c\in\Gamma\) and every
\(e\in\mathcal E_c\setminus\{e_c^0\}\), introduce one binary change
variable \(w_{c,e}\).  The keep choice needs no variable.  Put

\[
                         \sum_e w_{c,e}\le1
                         \qquad(c\in\Gamma).          \tag{3.1}
\]

If the sum is zero, retain \(e_c^0\); otherwise use the unique selected
alternative.  For every complementary owner \(v\in C\), impose the signed
balance row

\[
 \sum_{c,e}w_{c,e}
 \left({\bf1}_{v\in e}-{\bf1}_{v\in e_c^0}\right)=0.           \tag{3.2}
\]

### Theorem 3.1 (owner/lower-palette equivalence)

Equations (3.1)--(3.2) are equivalent to choosing exactly one edge of every
colour \(c\in\Gamma\) so that every complementary owner has the same internal
degree as in \(W[C]\).

#### Proof

For one colour, (3.1) selects either its old edge or exactly one alternative,
so every colour is represented exactly once.  The coefficient in (3.2) is
precisely the change in the degree of `v` caused by that replacement.  Thus
(3.2) is equivalent to equality of the old and new degree at every owner.
Conversely any one-edge-per-colour selection has a unique set of changed
colours and therefore a unique `w`; degree equality gives (3.2).
\(\square\)

The two complement owners incident with the frozen cross edges retain
internal degree one, and every other complement owner retains internal degree
two.  Consequently every solution of (3.1)--(3.2) is one path containing the
two boundary owners plus zero or more disjoint cycles.

## 4. Exact path and socket rows

Let \(x_{c,e}\) denote the derived selected-edge indicator, including the
implicit keep choice.  The complement is a single Hamilton path if and only if
the selected internal graph is acyclic.  An exact lazy family is

\[
        \sum_{c\in\Gamma}\ \,\sum_{e\in\mathcal E_c:e\subseteq S}
        x_{c,e}\le |S|-1
        \qquad(\varnothing\ne S\subseteq C).          \tag{4.1}
\]

Indeed there are already \(|C|-1=20201\) selected edges.  Thus (4.1) makes
the graph a spanning tree, and the degree pattern from Section 3 makes that
tree a path.  Adding the two frozen cross edges and the frozen marked path
then gives one Hamilton cycle on all `24310` owners, with every rank-eight
lower colour exactly once.

The two frozen cross incidences are

```text
marked owner 83766 -- lower colour 18230 -- complement owner 18294
marked owner 71930 -- lower colour  6394 -- complement owner 22778.
```

In the oriented zipper, `P_1=71930`, `P_a=83766`, `Q_1=18294`, and
`Q_b=22778`.  The first displayed cross edge is therefore the linear join
`P_a--Q_1`; the second is the owner-cycle closing edge `Q_b--P_1`.  The
closing edge is frozen topologically, but it is not automatically a linear
rank-ten interval of the zipper.

They preserve the marked bank and its length exactly.  The outward
complement-side port of either boundary owner is selected by the rethread.  If
a particular full socket is required, it is imposed by one endpoint incidence
row

\[
             \sum_{e\in\mathcal E_c:v\in e}x_{c,e}=1           \tag{4.2}
\]

for the prescribed boundary owner `v` and outward lower colour `c`, or by an
ALO over an allowed socket bank.  Thus socket choice is an explicit finite
state, not an implicit consequence of degree balance.

## 5. Exact signed upper-`q1` rows

Write the linear zipper as

\[
 Z=P_1,\ldots,P_a,F_0,\ldots,F_b,
 \quad F_0=P_a\cap Q_1,\quad
 F_i=Q_i\cap Q_{i+1},\quad F_b=Q_b\cap P_1.          \tag{5.1}
\]

The canonical linear rank-ten providers are

1. the `4107` unions \(P_i\cup P_{i+1}\);
2. the first-cross union \(P_a\cup Q_1\), represented by
   \((P_a,F_0,F_1)\); and
3. the `20201` internal-complement unions \(Q_i\cup Q_{i+1}\), represented
   by \((F_{i-1},F_i,F_{i+1})\).

There is no automatic provider attached to the closing edge \(Q_bP_1\),
because a linear interval cannot wrap from \(F_b\) to \(P_1\).

### Lemma 5.1 (linear zipper rank-ten reduction)

Every linear interval of `Z` whose union has rank ten contains one of the
canonical providers above with the same union.

#### Proof

Distinct consecutive lower colours give

\[
                         F_{i-1}\cup F_i=Q_i.        \tag{5.2}
\]

Thus any three consecutive facet rows have union
\(Q_i\cup Q_{i+1}\), of rank ten.  A facet-only rank-ten interval has length
at least three, so any contained triple is a canonical provider of the same
rank-ten set.  An interval wholly in the marked block reduces to an adjacent
marked pair.  Finally, an interval crossing the unique linear join either
contains two marked rows, or contains \((P_a,F_0,F_1)\), whose union is
\(P_a\cup Q_1\).  Equal ranks force the chosen provider union to equal the
whole interval union.  No linear interval crosses the closing edge.
\(\square\)

For a rank-ten target \(H\), let \(m_H^{Z,0}\) be its multiplicity in this
canonical provider multiset.  Equivalently, it is the current owner-cycle
edge load with the single closing-edge contribution
\({\bf1}_{Q_b\cup P_1=H}\) removed.  For an internal complement colour
\(c\), define

\[
 H_c^0=a_c\cup b_c,\qquad H(c,e)=\bigcup_{v\in e}v.           \tag{5.3}
\]

The exact canonical-provider multiplicity after the rethread is

\[
 m_H^Z(w)=m_H^{Z,0}+
 \sum_{c,e}w_{c,e}
 \left({\bf1}_{H(c,e)=H}-{\bf1}_{H_c^0=H}\right).             \tag{5.4}
\]

By Lemma 5.1, complete linear-zipper upper `q1` is equivalent to the `19448`
signed rows

\[
                         m_H^Z(w)\ge1.              \tag{5.5}
\]

These rows account for providers destroyed by a change as well as providers
created by it; requiring only the current holes would be unsound.  Counting
the closing owner edge as a baseline provider would also be unsound unless a
separate literal boundary witness were exhibited.

### Proposition 5.1 (no individual upper obstruction)

In the complete marked-preserving catalogue:

```text
current upper holes                         1900
columns adding a current hole              66223
distinct lower colours among those columns 16471
support per current hole                    10..45

fixed-pairing zero rows                       218
columns adding one of those rows             6419
distinct lower colours among those columns   5220
support per fixed-pairing zero row            10..45.
```

In particular every previously unreachable upper colour has at least one
column that creates it while leaving all marked owners untouched.  This is an
individual-support theorem, not a claim that such a column extends to a
simultaneous solution of (3.2), (4.1), and (5.5).

#### Proof

For each complement colour `c`, enumerate all unordered pairs of complement
rank-nine supersets of `c` except the current pair, and group them by their
rank-ten union.  Equations (2.4)--(2.6) prove completeness of the enumeration;
the authenticated census gives the displayed counts.  \(\square\)

## 6. Independent certificate

The complete catalogue is independently emitted by

```text
scratch/audit_ad_k17_opt28_complement_rethread_master_20260731.py
```

with artifacts

```text
script SHA-256   cbc997e2ff29b607de321211bbfce040106e593a87dc8d874767374ba82d8c0c
JSON SHA-256     36fe45cb80f9ae5565885640faa9f4c984001e6503777242a9c273abdbe534b7
payload SHA-256  4c551b0e6da95c691e38bb40df4f01441e6dc570f6f7f317c484358aa743dde7
column-stream    dc3c970185ad1fb985a2c620eeb5e7cf8a18403843f6c40a19b84a5cd47db139
```

The emitter reconstructs the marked set from the macro/packet artifacts,
checks the literal `4107+2+20201` edge partition, enumerates all `545721`
off-source columns, and verifies its payload after JSON round-trip.

## 7. Precise surviving gate

This theorem closes the *formulation* of the complementary facet-rail
rethread and proves that each of the `218` static holes has a column avoiding
the residence-clean marked bank.  It does not prove that all holes can be
served simultaneously without changing that bank, or even that the signed
master is feasible.  In particular:

* degree balance can correlate the individually abundant provider columns;
* the graphic cuts may force a provider-poor component merger;
* residence of the complementary path and the two boundary joins is not
  encoded by (3.1)--(5.5);
* upper depths at least two and literal lower/compiler rows remain;
* freezing the two cross edges preserves the owner-bank interface and scalar
  marked length, but not an integral common-cap matching.

The next exact finite gate is therefore the `545721`-column signed
degree-plus-upper master with lazy graphic cuts, followed by chronology CEGAR
for complement residence/deep shadows and the explicit socket bank (4.2).
