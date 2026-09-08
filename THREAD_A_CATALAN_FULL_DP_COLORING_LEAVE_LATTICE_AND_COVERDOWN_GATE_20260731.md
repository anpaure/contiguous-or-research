# The full Delcourt--Postle coloring: deficiency ledger, flux, and the aligned cover-down gate

Date: 2026-07-31
Status: exact whole-coloring ledger, exact soft-selection and private
cover-down lemmas, and a sharp abstract obstruction to obtaining an
absorber-aligned leave from coloring statistics alone.  No exact Catalan
side completion or AGCF perfect matching is claimed.

## 0. Result

Item 2295ROOT applies Delcourt--Postle to the four-uniform punctured
capacity-slot hypergraph \({\cal H}_Q\), for an arbitrarily preselected
admissible puncture set \(Q\).  The full coloring contains much more
first-moment information than its largest class:

1. the total deficiency of all classes and the omission count of every
   individual resource are exact;
2. all but an \(o(1)\) fraction of classes have \(o(P)\) deficiency;
3. all but an \(O(n^{-2/3})\) fraction of the resources are omitted by only an
   \(O(n^{-1/3}+D^{-alpha})\) fraction of the colors;
4. every class leave automatically lies in the affine integer incidence
   lattice of \({\cal H}_Q\), and obeys exact coordinate flux identities.

These facts do **not** force a class whose leave is a nonnegative union of
candidate edges.  A regular crown graph has an equitable near-perfect
coloring, exact resource incidence, lattice-valid leaves, and a
\(2\leftrightarrow2\) rectangle through every candidate, while every class
leave is a missing nonedge.  Thus lattice membership and universal local
trades do not imply edge-aligned cover-down.

There is also a type separation.  The coloring in item 2295ROOT is on the
four-uniform side-slot hypergraph.  The flux theorem and universal
\(2\leftrightarrow2\) absorber in item 2292AG live on the distinct
\((3n+1)\)-uniform antipodal-geodesic resource hypergraph.  No exact
incidence map between those two systems is currently proved.

The surviving positive theorem is a private-reservoir Hall lemma: if one
color leave already decomposes into candidate edges and their compatible
trade-mate lists satisfy Hall with private supports, then simultaneous
\(2\leftrightarrow2\) switches complete it.  What remains is an
aligned-color or cross-color recoloring theorem which creates precisely
that semigroup decomposition.

## 1. Full-coloring notation

Fix the short-cycle cutoff \(L\) and the Delcourt--Postle exponent
\(\alpha=\alpha(L,\beta)>0\).  Put

\[
 D=2(n+1)(n+2),\qquad
 K_D=\left\lceil D(1+D^{-\alpha})\right\rceil=D+s,
 \qquad s=\left\lceil D^{1-\alpha}\right\rceil.       \tag{1.1}
\]

Let

\[
                 E_Q=E({\cal H}_Q),\qquad e_Q=|E_Q|.
\]

The theorem gives a proper conflict-free coloring of all atoms using
\(k\le K_D\) nonempty color classes

\[
                         M_1,\ldots,M_k.              \tag{1.2}
\]

Each \(M_i\) is a matching in \({\cal H}_Q\), avoids every prescribed
projected cycle of length at most \(L\), and has the matching ceiling
\(|M_i|\le P\).  Define

\[
                         \delta_i=P-|M_i|.            \tag{1.3}
\]

The resource vertices have three types: the \(P\) punctured lower colors
\({\cal D}\), the \(P\) upper colors \({\cal V}\), and the slot bank
\({\cal S}\) of order

\[
                         |{\cal S}|=2N-C.             \tag{1.4}
\]

## 2. Exact deficiency distribution

### Theorem 2.1 (whole-palette deficiency ledger)

For the actual nonempty coloring,

\[
              \boxed{\sum_{i=1}^k\delta_i=kP-e_Q.}   \tag{2.1}
\]

Moreover

\[
2n(n-1)P-2C(n^2-1)\le e_Q\le2n(n-1)P,              \tag{2.2}
\]

and

\[
                 {2C(n^2-1)\over P}=8n+12+{4\over n}.              \tag{2.3}
\]

If the palette is padded by empty classes to exactly \(K_D=D+s\) colors,
then

\[
 (s+8n+4)P
 \le K_DP-e_Q
 \le\left(s+16n+16+{4\over n}\right)P.              \tag{2.4}
\]

The lower bound in (2.4) partly records the artificially padded empty
classes.  For the actual coloring only

\[
 0\le kP-e_Q
 \le\left(s+16n+16+{4\over n}\right)P               \tag{2.5}
\]

is forced.

#### Proof

The classes partition \(E_Q\), proving (2.1).  The two bounds in (2.2)
are the exact capacity-slot edge ledger.  Since

\[
 D-2n(n-1)=8n+4
\]

and the puncture loss divided by \(P\) is (2.3), subtracting (2.2) from
\(DP\) gives

\[
 (8n+4)P\le DP-e_Q
 \le\left(16n+16+{4\over n}\right)P.
\]

Adding \(sP\) proves (2.4), and \(k\le K_D\) gives (2.5). \(\square\)

Define

\[
 \rho_n={s+16n+16+4/n\over D+s}
       =O(D^{-\alpha}+n^{-1}).                       \tag{2.6}
\]

### Corollary 2.2 (the complete forced distribution statement)

\[
 {1\over k}\sum_i\delta_i\le\rho_nP,                \tag{2.7}
\]

and for every \(\varepsilon>0\),

\[
 {1\over k}|\{i:\delta_i>\varepsilon P\}|
 \le {\rho_n\over\varepsilon}.                      \tag{2.8}
\]

Consequently at least half the classes have deficiency at most
\(2\rho_nP=o_L(P)\), and a \(1-\sqrt{\rho_n}\) fraction have deficiency
at most \(\sqrt{\rho_n}P=o_L(P)\).

#### Proof

The function \(P-e_Q/x\) is increasing in \(x\).  Hence the actual mean
in (2.1), which is \(P-e_Q/k\), is at most the padded mean
\(P-e_Q/K_D\); now use (2.4).  Equation (2.8) is Markov's inequality.
\(\square\)

Nothing in the coloring theorem gives a second-moment improvement.  From
\(0\le\delta_i\le P\) one has only

\[
 {\bigl(\sum_i\delta_i\bigr)^2\over k}
 \le\sum_i\delta_i^2
 \le P\sum_i\delta_i.                               \tag{2.9}
\]

Thus the theorem is compatible with concentrating essentially all
deficiency in an \(O(\rho_n)\) fraction of bad classes.  It proves many
large classes, not equitability or a higher-order deficiency law.

Here and below, an assertion obtained by sending \(L\) to infinity means:
first apply the coloring theorem for each fixed \(L\), with its resulting
exponent \(\alpha(L,\beta)\), and only then diagonalize in \(L\).  No estimate
uniform in a growing \(L\) is being used.

## 3. Exact resource incidence across colors

For a resource vertex \(v\), let \(d(v)\) be its degree in \({\cal H}_Q\),
and let \(L_i\) be the vertex leave of \(M_i\).

### Theorem 3.1 (one-resource decomposition)

For every resource \(v\),

\[
 \sum_{i=1}^k{\bf1}[v\in V(M_i)]=d(v),\qquad
 \sum_{i=1}^k{\bf1}[v\in L_i]=k-d(v).                \tag{3.1}
\]

For every resource set \(S\),

\[
             \sum_i|S\cap L_i|=k|S|-\sum_{v\in S}d(v).            \tag{3.2}
\]

In particular, on either outer shore,

\[
 |L_i\cap{\cal D}|=|L_i\cap{\cal V}|=\delta_i
 \quad(i\in[k]),                                                   \tag{3.3}
\]

and therefore

\[
 \sum_i|L_i\cap{\cal D}|=
 \sum_i|L_i\cap{\cal V}|=kP-e_Q.                   \tag{3.4}
\]

Every class leaves exactly

\[
 |L_i\cap{\cal S}|=|{\cal S}|-2|M_i|
                   =(C-2\operatorname {Cat}_n)+2\delta_i          \tag{3.5}
\]

unused slots.

#### Proof

Properness makes the colors on the \(d(v)\) atoms through \(v\) distinct,
proving (3.1).  Sum over \(v\in S\) for (3.2).  Each atom uses one vertex
on each outer shore and two slots, giving (3.3)--(3.5). \(\square\)

For nonnegative resource weights \(w_v\), a uniform random color has

\[
 \mathbb E_i\,w(L_i)
 ={1\over k}\sum_vw_v(k-d(v)).                       \tag{3.6}
\]

This gives an exact soft selection theorem for any one additive risk.  For
finitely many risks \(w^{(j)}\), numbers \(\lambda_j>1\) with
\(\sum_j\lambda_j^{-1}<1\) guarantee one class satisfying

\[
 w^{(j)}(L_i)
 \le{\lambda_j\over k}\sum_vw_v^{(j)}(k-d(v))
 \quad\text{for every }j.                            \tag{3.7}
\]

This is the union bound and Markov.  It does not enforce an equality,
congruence, Hall condition, or nonnegative edge decomposition.

The deterministic almost-regularity theorem gives more one-resource
information.  All but \(O(n^{-2/3}|V({\cal H}_Q)|)\) resources have

\[
                         d(v)=2n^2+O(n^{5/3}).        \tag{3.8}
\]

Since \(k\le D+s\) and \(k=\Theta(n^2)\), such a resource is omitted by
only an

\[
                         O(n^{-1/3}+D^{-\alpha})      \tag{3.9}
\]

fraction of the colors.  No pair-resource concentration follows.  If
\(d(v,w)\) is the hypergraph codegree and \(c(v,w)\) denotes the number
of colors covering both resources, then every common atom has a distinct
color and the strongest immediate bounds are

\[
 \max\{d(v,w),d(v)+d(w)-k\}
 \le c(v,w)\le\min\{d(v),d(w)\}.                                 \tag{3.10}
\]

This absence of joint incidence is exactly where absorber alignment can
fail.

There is, nevertheless, one exact pair-of-classes ledger.  Put
\(R_i=V(M_i)\).  Double-counting each resource over unordered pairs of
colors gives

\[
 \sum_{i<j}|R_i\cap R_j|=\sum_v {d(v)\choose2},\qquad
 \sum_{i<j}|R_i\mathbin\triangle R_j|
     =\sum_v d(v)(k-d(v)).                              \tag{3.11}
\]

These averages underpin the almost-regular exchange core of item 2297DP,
but they do not identify a pair whose terminal components split into the
private trades required below.

## 4. Cycle pruning across the entire coloring

Let \(Z_i\subseteq M_i\) contain one atom from every projected physical
cycle of \(M_i\), and put \(z_i=|Z_i|\).  Since every cycle has length at
least \(L+1\),

\[
 z_i\le {|M_i|\over L+1},\qquad
 \sum_i z_i\le {e_Q\over L+1}.                       \tag{4.1}
\]

The forest class \(F_i=M_i\setminus Z_i\) has deficiency

\[
                         \delta_i^{\rm F}=\delta_i+z_i,            \tag{4.2}
\]

and hence

\[
 {1\over k}\sum_i\delta_i^{\rm F}
 \le\left(\rho_n+{1\over L+1}\right)P.              \tag{4.3}
\]

The added leave \(V(Z_i)\) is already a disjoint union of complete atom
edges.  Thus cycle pruning creates an edge-aligned part of the leave.  The
hard part is the pre-existing raw leave \(L_i\), whose unmatched outer
resources need not support even one candidate atom.

For every resource \(v\), the post-pruning omission count is exactly

\[
 k-d(v)+|\{e\in\bigcup_i Z_i:v\in e\}|.              \tag{4.4}
\]

Typewise, the total added omission is exactly \(\sum_i z_i\) on each outer
shore and \(2\sum_i z_i\) on the slots.  Its distribution among individual
resources is uncontrolled.  Hence arbitrary cycle-breaking choices need not
retain the one-resource balance of the raw coloring.

## 5. What “flux aligned” means here

Let \(A_Q\) be the resource-by-atom incidence matrix of \({\cal H}_Q\).
Every raw class leave satisfies

\[
                  {\bf1}-\chi_{L_i}=A_Q\chi_{M_i},
 \qquad
                  \chi_{L_i}\in{\bf1}+\operatorname {im}_{\mathbb Z}A_Q.
                                                               \tag{5.1}
\]

Thus affine integer-lattice membership is automatic for **every** class;
it is not a selection property.

There are explicit coordinate flux rows.  An atom indexed by
\(D\subset V=D\cup\{a,b\}\) uses physical slots at
\(x=D+a\) and \(y=D+b\).  For every ground coordinate \(u\),

\[
 {\bf1}[u\in x]+{\bf1}[u\in y]
 ={\bf1}[u\in D]+{\bf1}[u\in V].                    \tag{5.2}
\]

Therefore, if \(\Phi_u\) is slot incidence containing \(u\) minus lower
and upper incidence containing \(u\), then

\[
                    \Phi_u(A_Q\chi_e)=0,
 \qquad             \Phi_u(\chi_{L_i})=\Phi_u({\bf1})             \tag{5.3}
\]

for every atom \(e\) and every color \(i\).  The coarse relation is

\[
 |L_i\cap{\cal S}|-|L_i\cap{\cal D}|-|L_i\cap{\cal V}|
                         =C-2\operatorname {Cat}_n.  \tag{5.4}
\]

Deleting the atoms \(Z_i\) adds columns of \(A_Q\), so (5.1)--(5.4)
remain true after cycle pruning.

These are the diamond-flux rows of the four-uniform side system.  They are
not the AGCF identities

\[
 |R_M|=(n+1)t,quad |R_L|=|R_U|=nt,quad
 m_u(R)=u_u(R)=\ell_u(R)+t,                          \tag{5.5}
\]

which belong to the separate complement-geodesic resource hypergraph.
There is no proved map taking a side-slot color leave to an AGCF leave.
SBE is upstream and is unchanged because \(Q\) was fixed before coloring.
The downstream common-cap row is not a vertex or flux row of
\({\cal H}_Q\), so no averaging assertion about it is made.

## 6. If the AGCF hypergraph itself had such a coloring

The preceding type distinction does not make the whole-coloring idea
useless for AGCF.  It gives an exact quantitative target.

Let \({\cal G}_n\) be the \((3n+1)\)-uniform AGCF resource hypergraph,
let

\[
 D_A={n+1\over2}(n!)^2,qquad T=\operatorname {Cat}_n,              \tag{6.1}
\]

and suppose all candidates are properly colored into \(\kappa=D_A+r\)
matching classes \(J_1,\ldots,J_\kappa\).  Properness forces
\(\kappa\ge D_A\), because every resource has degree \(D_A\).

### Theorem 6.1 (regular whole-coloring ledger)

If \(t_i=T-|J_i|\), then

\[
                    \sum_i t_i=rT,                  \tag{6.2}
\]

every resource is omitted by exactly \(r\) classes, and every class leave
obeys the AGCF flux identities (5.5) with parameter \(t=t_i\).

If

\[
                              rT<\kappa,              \tag{6.3}
\]

then some color class is a perfect matching.

#### Proof

Counting incidences on the middle shore gives
\(|E({\cal G}_n)|=D_AT\).  Summing class sizes proves (6.2).  Properness
uses the \(D_A\) edges through each resource in distinct colors, proving
the omission statement.  Every matching leave satisfies (5.5) by the
pathwise flux theorem.  Finally the nonnegative integers \(t_i\) cannot
all be positive when their sum is smaller than the number of classes.
\(\square\)

In particular, a coloring estimate

\[
                  \kappa\le D_A(1+D_A^{-\alpha_n})   \tag{6.4}
\]

would force a perfect class whenever

\[
                         T<D_A^{\alpha_n}.            \tag{6.5}
\]

The exact exponent threshold is

\[
 {\log T\over\log D_A}
       ={\log2\over\log n}(1+o(1)).                 \tag{6.6}
\]

Thus any fixed positive exponent would be more than enough.  The current
Delcourt--Postle invocation does **not** prove (6.4): its uniformities are
fixed before the degree tends to infinity, whereas the AGCF rank is
\(3n+1\), and no lower bound on the resulting \(\alpha_n\) is available.

Even when (6.3) fails, all flux and divisibility identities proved in item
2292AG still need no averaging—every class already has them.  A full
all-\(n\) Smith-normal-form description of the AGCF incidence lattice is not
proved.  In either formulation, the remaining nonlinear issue is
candidate-edge alignment of the leave.

## 7. Sharp obstruction: equitable coloring plus universal trades is insufficient

Let \(p\ge5\) be odd, with left and right resources

\[
                    \{L_i:i\in\mathbb Z_p\},\qquad
                    \{U_j:j\in\mathbb Z_p\}.
\]

Take the crown graph

\[
                  H=K_{p,p}-\{L_iU_i:i\in\mathbb Z_p\}.            \tag{7.1}
\]

Color the edge \(L_iU_j\), \(i\ne j\), by

\[
                         c={i+j\over2}\pmod p.        \tag{7.2}
\]

### Theorem 7.1 (lattice-valid nonaligned leaves)

The coloring (7.2) has all of the following properties.

1. It has \(p\) classes, each a matching of size \(p-1\).
2. Every resource occurs in exactly \(p-1\) classes.
3. Class \(c\) leaves exactly \(\{L_c,U_c\}\).
4. Every candidate edge of \(H\) lies in a \(2\leftrightarrow2\) rectangle.
5. Every class leave lies in the full integer edge-incidence lattice of
   \(H\).
6. No class leave is candidate-shaped.

#### Proof

For fixed \(c\),

\[
                    M_c=\{L_iU_{2c-i}:i\ne c\}.       \tag{7.3}
\]

This is a size-\(p-1\) matching and omits precisely \(L_c,U_c\).  Every
off-diagonal pair \((i,j)\) has the unique color \((i+j)/2\), proving the
first three statements.

For an edge \(L_iU_j\), choose \(k\notin\{i,j\}\) and then
\(\ell\notin\{i,j,k\}\).  The four off-diagonal edges on
\(\{L_i,L_k\}\times\{U_j,U_\ell\}\) form the required rectangle.

For distinct \(a,b,c\),

\[
 {\bf e}_{L_c}+{\bf e}_{U_c}
 =\chi_{L_cU_a}+\chi_{L_bU_c}-\chi_{L_bU_a},          \tag{7.4}
\]

so the leave is in the integer edge lattice.  But \(L_cU_c\notin E(H)\),
and a two-resource leave can be a nonnegative disjoint union of candidate
edges only if it is one candidate edge.  Hence no leave is candidate-shaped.
\(\square\)

This counterexample already has the strongest possible class-size
distribution and one-resource incidence.  It shows that neither averaging,
exact lattice membership, nor a universal trade through every **existing**
candidate forces a leave inside the nonnegative candidate semigroup.  It
does not exclude compound cross-class recoloring or a larger global
absorber.

## 8. A rigorous private-reservoir cover-down lemma

The counterexample identifies the exact positive hypothesis that is
missing.

### Theorem 8.1 (private \(2\leftrightarrow2\) cover-down)

Let \({\cal H}\) be a resource hypergraph and \(M\) a matching.  Suppose
its essential leave consists of genuinely uncovered resources and is the
disjoint union of full candidate supports

\[
                         L=A_1\mathbin{\dot\cup}\cdots
                              \mathbin{\dot\cup}A_t.  \tag{8.1}
\]

Thus \(A_i\cap V(M)=\varnothing\) for every \(i\), and the \(A_i\) are
pairwise resource-disjoint.

For each \(i\), let \({\cal B}_i\subseteq M\) be a list of possible trade
mates.  Assume:

1. for every \(B\in{\cal B}_i\) there are candidates \(C(i,B),D(i,B)\)
   with
   \[
             \chi_{A_i}+\chi_B
              =\chi_{C(i,B)}+\chi_{D(i,B)};           \tag{8.2}
   \]
2. apart from \(B\), the support of this trade is disjoint from \(M\);
3. privacy holds before the Hall choice: for every \(i\ne j\), every
   \(B\in{\cal B}_i\), and every \(B'\in{\cal B}_j\) with \(B\ne B'\),
   the complete supports of the two trades are disjoint; and
4. the mate lists satisfy Hall:
   \[
                  \left|\bigcup_{i\in I}{\cal B}_i\right|\ge|I|
                  \qquad(I\subseteq[t]).             \tag{8.3}
   \]

Then \(M\) extends, by simultaneous \(2\leftrightarrow2\) switches, to a
matching covering its essential resource bank exactly.

#### Proof

Hall chooses distinct mates \(B_i\in{\cal B}_i\).  Replace every \(B_i\)
by \(C(i,B_i),D(i,B_i)\).  Conditions 2--3 make all replacements mutually
compatible and compatible with the untouched part of \(M\).  Summing
(8.2) shows that the new edges cover precisely the old resources of the
mates together with all of \(L\). \(\square\)

If conflict-freeness, physical acyclicity, residence, or common-cap state
must survive, family-level guard compatibility must be included in the
definition of a legal/private trade.  Individual legality and even
resource-disjointness do not exclude a physical cycle or a repeated physical
owner spanning several trades.  If compatibility depends on which Hall
representatives are selected, ordinary Hall must be replaced by a
conflict-aware independent-transversal theorem.  None of these guards follows
from (8.2).

There is one useful color-selection corollary.  Let \({\cal A}\) be the
set of color classes which admit an aligned decomposition (8.1), legal
cycle pruning, and the private Hall system (8.3), and put
\(a_n=|{\cal A}|/k\).  Then

\[
 \min_{i\in{\cal A}}\delta_i^{\rm F}
 \le {\rho_n+1/(L+1)\over a_n}P.                    \tag{8.4}
\]

Hence

\[
                         a_n\gg\rho_n+L^{-1}          \tag{8.5}
\]

would produce an absorber-compatible \(P-o(P)\) forest.  The
Delcourt--Postle theorem gives no positive lower bound on \(a_n\), as
Theorem 7.1 demonstrates abstractly.

## 9. Exact boundary

The full coloring proves a genuine distributed reservoir statement:

* many classes have \(o(P)\) deficiency;
* almost every individual resource is present in almost every color; and
* every leave satisfies all linear incidence-flux laws of its own host.

It does not prove pair or higher missing-resource correlation, a
candidate-edge decomposition of any leave, trade-mate Hall, or preservation
of the downstream common cap.  Therefore coloring alone cannot close exact
cover-down.

The minimum new theorem is one of:

1. a positive-density aligned-color theorem proving (8.5);
2. a cross-color alternating-recoloring theorem which drives one raw leave
   into the candidate semigroup while keeping the physical guards; or
3. for AGCF, a growing-rank coloring bound with exponent satisfying (6.5),
   which would actually yield a perfect color class before absorption.

SBE and common-basis concentration are not part of this remaining step.
They concern the already fixed puncture bank \(Q\).  Exact common-cap,
residence and deeper-shadow compatibility remain additional rows unless
they are explicitly built into the legal trade catalogue.

## 10. Adversarial audit

1. The deficiency distribution uses only the actual color partition and
   the exact edge ledger; no equitable-coloring property is assumed.
2. The almost-regularity statement is one-resource only.  Equation (3.10)
   records the absence of pair control.
3. Affine lattice membership is automatic and is strictly weaker than a
   nonnegative candidate decomposition.
4. The crown graph is an abstract obstruction, not a Catalan
   counterexample.  It refutes an inference from coloring statistics and
   universal local trades, not every Boolean-specific cover-down theorem.
5. The AGCF coloring theorem in Section 6 is conditional.  The present
   Delcourt--Postle result has fixed uniformity and gives no usable
   \(\alpha_n\) for rank \(3n+1\).
6. Cycle-pruning leaves are edge-aligned, but the raw color deficiency is
   not; this is why deleting long cycles does not solve the absorber gate.
7. Common-cap and physical guard preservation are not consequences of the
   incidence equality (8.2); they must be checked trade by trade.
