# Third-wave lane M: the physical rank-seven lift at \(k=11\)

Date: 2026-07-24

## 1. Verdict

Assume the audited zero-margin \(k=11\), length-\(465\) normal form and the
ordered rank-five/rank-six matching from
MATH_ATTACK_M_K11_EXTENSION_LABELS_20260724.md.

No contradiction is obtained.

The rank-seven forest can, however, be lifted all the way back to the
physical word. The resulting theorem has four exact parts.

1. Every one of the \(462-c\) projected six-forest edges is represented by
   one literal interval of width at most four. Its rank-seven complement is
   exactly the four-set simultaneously absent from every physical entry of
   that interval.

2. In the central rank-at-most-three segment, a rank-seven color
   \(Q=[11]\setminus Y\) is represented exactly by length-five subwindows
   of maximal joint \(Y\)-zero-runs. If those run lengths are
   \(\ell_1,\ldots,\ell_b\geq5\), then
   \[
   \boxed{\sum_{j=1}^b(\ell_j-3)\leq7.}
   \]
   Hence a joint four-coordinate zero-run has length at most ten, a fixed
   rank-seven color has at most three separated central blocks, and its
   literal central multiplicity is at most six.

3. Every external-headed rank-seven edge is an exact directed complement
   flag
   \[
   Y\subset D\subset C,\qquad (|Y|,|D|,|C|)=(4,5,6),
   \]
   decorated by two distinct coordinates. The matching coordinate obeys
   the audited factor-three external-offset capacity. The full two-label
   pair obeys a new factor-four physical exposure capacity.

4. The central joint-zero data, the simple rank-seven head-label matrix,
   and the external flags satisfy exact nested Hall inequalities. At most
   two inward-pointing external/central interfaces are outside the
   external-anchor Hall system.

The global support and duplicate conclusions remain
\[
\boxed{z_7\geq319,\qquad M_7:=330-z_7\leq11,}
\]
\[
\boxed{
\Delta_7:=\sum_Q(t_Q-1)_+
=132-c+M_7,\qquad126\leq\Delta_7\leq137.
}
\]
The new lift localizes every unit of \(\Delta_7\) as a central lazy fold, a
separated central return, an outer repetition, or a central/outer support
overlap. This localization does not raise the universal lower bound
\(\Delta_7\geq126\) or force a contradiction.

The strongest unresolved gate is now set-valued and physical:

> simultaneously realize the \(330\) joint four-coordinate zero-run
> systems, the simple head-label matrix, the external depth-two flags, and
> the directed anchor exposures in the fixed endpoint order.

All arguments below are deterministic and integral. No web lookup, finite
search, solver, random experiment, or computational enumeration is used.

## 2. Frozen setup

Let
\[
\Omega=[11].
\]
Throughout, the physical width of an interval \([a,b]\) is its endpoint
span \(b-a\), equal to its number of entries minus one.
The physical word has positions \(0,\ldots,464\), with entry \(B_p\) at
position \(p\). Its central rank-at-most-three segment is
\[
[L,R],\qquad m=R-L+1,
\]
and
\[
A_i=B_{L+i}\qquad(0\leq i<m).
\]
Put
\[
E=465-m,\qquad q=m-3=462-E.
\tag{2.1}
\]

The selected rank-five and rank-six witnesses are in their common strict
endpoint order:
\[
I_j=[\ell_j,r_j],\qquad
J_j=[u_j,v_j],\qquad0\leq j<462.
\tag{2.2}
\]
Their colors are
\[
S_j=\operatorname{OR}(I_j),\qquad
U_j=\operatorname{OR}(J_j),
\tag{2.3}
\]
and
\[
S_j\subset U_j,\qquad M(S_j)=U_j
\tag{2.4}
\]
is a perfect inclusion matching.

The rank-five offset schedule has \(c\leq6\) nonempty state blocks. After
deleting the state transitions, the middle-level vertices form \(c\)
alternating paths. Projecting onto the six-set vertices gives a spanning
linear forest
\[
G_6\subset J(11,6)
\tag{2.5}
\]
with
\[
|E(G_6)|=462-c.
\tag{2.6}
\]

Orient one component as
\[
S_0,U_0,S_1,U_1,\ldots,S_r,U_r,
\qquad U_i=M(S_i).
\tag{2.7}
\]
Define
\[
\alpha_i=U_i\setminus S_i
\quad(0\leq i\leq r),
\qquad
\beta_i=U_i\setminus S_{i+1}
\quad(0\leq i<r).
\tag{2.8}
\]
For \(0\leq i<r\), the transition \(U_i\to U_{i+1}\) loses
\(\beta_i\) and gains \(\alpha_{i+1}\).

For every six-forest edge \(0\leq i<r\), put
\[
Q_i=U_i\cup U_{i+1}\in\binom{\Omega}{7}.
\tag{2.9}
\]
For \(Q\in\binom{\Omega}{7}\), let \(t_Q\) be its multiplicity among all
these edges.

The imported rank-seven theorem gives
\[
0\leq t_Q\leq6,
\tag{2.10}
\]
\[
z_7=\#\{Q:t_Q>0\}\geq319,
\qquad
M_7=330-z_7\leq11,
\tag{2.11}
\]
and
\[
\Delta_7
=\sum_Q(t_Q-1)_+
=462-c-z_7
=132-c+M_7.
\tag{2.12}
\]

The central windows are
\[
C_i=A_i\cup A_{i+1}\cup A_{i+2},
\qquad
T_i=A_i\cup A_{i+1}\cup A_{i+2}\cup A_{i+3}.
\tag{2.13}
\]
All \(T_i\) are distinct six-sets. Every \(C_i\) except the exceptional
seam triple \(H=C_s\) is a distinct five-set. Every ordinary five-window
has rank seven. An internal seam-centered five-window has rank
\(7+\eta\), with \(\eta\geq0\).

Let
\[
b_H=
\begin{cases}
1,&\text{the seam is at a central endpoint},\\
2,&\text{the seam is internal}.
\end{cases}
\tag{2.14}
\]
Thus the internal central six-path core has \(b_H\) path pieces.

## 3. Literal hulls and exact \(4\subset7\) flags

### Theorem 3.1: every six-forest edge has a literal rank-seven hull

For every retained adjacent pair \(J_j,J_{j+1}\),
\[
K_j=J_j\cup J_{j+1}
\tag{3.1}
\]
is one literal interval and
\[
\operatorname{OR}(K_j)=U_j\cup U_{j+1}
\tag{3.2}
\]
has rank seven. Its physical width is at most four.

The exact hull-offset schedule is
\[
\boxed{02^*,\ 03^*,\ 04^*,\ 14^*,\ 24^*.}
\tag{3.3}
\]

#### Proof

Inside rank-five states \(00,01,02\),
\[
I_j\cup I_{j+1}\subseteq J_j,
\tag{3.4}
\]
while inside states \(13,23,33\),
\[
I_j\cup I_{j+1}\subseteq J_{j+1}.
\tag{3.5}
\]
Thus \(J_j,J_{j+1}\) overlap through a literal selected \(I\)-interval.
Their union is contiguous. Its OR is the union of two adjacent six-sets,
which has rank seven.

Writing the rank-six schedule as
\[
01^*02^*03^*13^*23^*
\]
and taking consecutive interval hulls gives (3.3). Every displayed state
has endpoint difference at most four.
\(\square\)

This is a physical statement for the actual chain-A forest. The converse
abstract directed-forest theorem does not imply it for an arbitrary
middle-level cover.

### Theorem 3.2: complement-zero encoding

For a forest edge \(e\), let \(K_e\) be its literal hull, let
\[
Q_e=\operatorname{OR}(K_e),
\qquad
Y_e=\Omega\setminus Q_e.
\tag{3.6}
\]
Then
\[
\boxed{
Y_e=\{x\in\Omega:B_p\not\ni x
\text{ for every }p\in K_e\}.
}
\tag{3.7}
\]
Consequently, for every \(Y\in\binom{\Omega}{4}\), with
\(Q=\Omega\setminus Y\),
\[
\boxed{
t_Q
=\#\{e: B_p\cap Y=\varnothing
\text{ for every }p\in K_e\}.
}
\tag{3.8}
\]

#### Proof

The OR of the entries on \(K_e\) is exactly \(Q_e\). A coordinate is
outside that OR exactly when it is absent from every entry of the interval.
Since \(|Q_e|=7\), its complement has size four. Equation (3.8) is the
same statement counted over all edges.
\(\square\)

Thus the \(319/330\) support theorem says that at least \(319\) of the
\(330\) four-sets occur as exact simultaneous-zero sets of literal forest
hulls.

### Theorem 3.3: the exact \(4\subset7\) flag

Put
\[
R_i=S_i\cap S_{i+1}.
\tag{3.9}
\]
Then
\[
\begin{aligned}
S_i&=R_i\sqcup\{\beta_i\},\\
S_{i+1}&=R_i\sqcup\{\alpha_i\},\\
U_i&=R_i\sqcup\{\alpha_i,\beta_i\},\\
U_{i+1}&=R_i\sqcup\{\alpha_i,\alpha_{i+1}\},\\
Q_i&=R_i\sqcup\{\alpha_i,\beta_i,\alpha_{i+1}\}.
\end{aligned}
\tag{3.10}
\]
The three coordinates
\[
\alpha_i,\ \beta_i,\ \alpha_{i+1}
\tag{3.11}
\]
are pairwise distinct. Hence every forest edge gives an ordered partition
\[
\boxed{
\Omega=R_i\sqcup Y_i\sqcup
\{\alpha_i,\beta_i,\alpha_{i+1}\}
}
\tag{3.12}
\]
of type \(4+4+3\), with
\[
R_i\subset Q_i.
\]

#### Proof

The first four identities follow by comparing the two representations of
\(U_i\) and the matching representation of \(U_{i+1}\). The coordinates
\(\alpha_i,\beta_i\) are distinct because one is gained and one is lost.
Also \(\alpha_i\in S_{i+1}\), whereas
\(\alpha_{i+1}\notin S_{i+1}\). Finally, if
\(\beta_i=\alpha_{i+1}\), then \(U_i=U_{i+1}\), contrary to the
injectivity of the selected rank-six row. The last identity follows.
\(\square\)

## 4. Two exact decompositions of the duplicate excess

### 4.1 Lazy folds and separated returns

Along each six-path, regard
\[
Q_0,Q_1,\ldots,Q_{r-1}
\tag{4.1}
\]
as a color word. For a fixed \(Q\), let \(b_Q\) be the number of maximal
constant \(Q\)-blocks over all components. Define
\[
\mathcal A_7=\sum_Q(t_Q-b_Q),
\tag{4.2}
\]
\[
\mathcal S_7=\sum_{Q:t_Q>0}(b_Q-1).
\tag{4.3}
\]

### Theorem 4.1: exact lazy-walk identity

\[
\boxed{
\Delta_7=\mathcal A_7+\mathcal S_7=132-c+M_7.
}
\tag{4.4}
\]

Here \(\mathcal A_7\) is the number of adjacent equal rank-seven hull
pairs, and \(\mathcal S_7\) is the number of separated or cross-component
reappearances.

If
\[
Q_i=Q_{i+1}=Q,
\]
then
\[
x=Q\setminus U_{i+1}
\;=\;\beta_i\;=\;\alpha_{i+2}
\tag{4.5}
\]
is the unique restitution coordinate: the incoming six-transition loses
\(x\), and the outgoing six-transition gains \(x\). Thus lazy turns with
restitution coordinate \(x\) are exactly the internal singleton
\(x\)-zero-runs on the six-paths.

If \(\mathcal A_x\) counts them, then
\[
\boxed{
\mathcal A_x
\leq
\min\{42-\pi_x,\ 42-\mu_x+\tau_x\}.
}
\tag{4.6}
\]
Here \(\pi_x\) counts path-start matching labels, \(\mu_x\) root six-set
incidences, and \(\tau_x\) start five-set incidences.

#### Proof

A block of \(t\) equal colors contributes \(t-1\) adjacent equalities.
For each supported color,
\[
t_Q-1=(t_Q-b_Q)+(b_Q-1).
\]
Summing gives (4.4).

If two consecutive hulls equal \(Q\), their middle six-set is the facet
\(Q\setminus\{x\}\). The incoming neighboring facet contains \(x\), so
the incoming transition deletes \(x\); the outgoing neighboring facet
contains \(x\), so the outgoing transition gains \(x\). The total gain and
loss counts are respectively
\[
42-\pi_x,\qquad42-\mu_x+\tau_x,
\]
which gives (4.6).
\(\square\)

### 4.2 Joint \(4\subset7\) flags

Let
\[
m_{R,Q}=\#\{i:R_i=R,\ Q_i=Q\}.
\tag{4.7}
\]
For \(Q\), put
\[
d_Q=\#\{R:m_{R,Q}>0\},
\qquad
j_Q=\#\{R:m_{R,Q}=2\}.
\tag{4.8}
\]

### Theorem 4.2: exact core decomposition

For every \(R\subset Q\), \((|R|,|Q|)=(4,7)\),
\[
\boxed{m_{R,Q}\leq2.}
\tag{4.9}
\]
Moreover,
\[
\boxed{
\Delta_7
=\sum_Q(d_Q-1)_+
+\sum_Qj_Q.
}
\tag{4.10}
\]

Every joint flag with multiplicity two consists of two adjacent forest
edges. Such a doubled joint flag can occur only in the literal rank-five
states \(00\) or \(33\).

#### Proof

For fixed \(R\subset Q\), the possible five-set vertices are the three
petals
\[
R\cup\{x\},\qquad x\in Q\setminus R.
\]
Their possible edges form a triangle. A linear forest contains at most two
of those edges, proving (4.9).

Since every nonzero \(m_{R,Q}\) is one or two,
\[
t_Q=d_Q+j_Q.
\]
Subtract one for each used \(Q\) and sum to get (4.10).

Two selected edges from the three-petal triangle share a vertex, so in the
linear forest they are consecutive. Their lower colors are equal to \(R\).
An adjacent repetition of a rank-four lower color is an internal
coordinate pattern \(010\) on the rank-five path. Sliding physical
windows of length at least two cannot have this pattern: the union of the
two flanking windows covers the middle window. Therefore it is possible
only in the singleton states \(00,33\).
\(\square\)

If \(n_{00},n_{33}\) are the vertex counts in those two literal blocks,
\[
\boxed{
\sum_Qj_Q
\leq(n_{00}-2)_++(n_{33}-2)_+.
}
\tag{4.11}
\]
In the zero-margin slices this is at most \(131\) when \(n_5=133\), and at
most \(130\) when \(n_5=132\). These bounds remain compatible with
\(\Delta_7\geq126\).

## 5. Exact central joint-zero geometry

Fix
\[
Y\in\binom{\Omega}{4},
\qquad
Q=\Omega\setminus Y.
\tag{5.1}
\]
Call a central index \(i\) \(Y\)-zero if
\[
A_i\cap Y=\varnothing.
\]
Let the maximal \(Y\)-zero-runs have lengths \(\ell\). Define
\[
V_Y=\sum_{\ell}(\ell-3)_+,
\qquad
W_Y=\sum_{\ell}(\ell-4)_+,
\tag{5.2}
\]
\[
b_Y=\#\{\ell:\ell\geq5\},
\qquad
u_{4,Y}=\#\{\ell:\ell=4\}.
\tag{5.3}
\]

### Theorem 5.1: four-window facets and five-window colors

\[
\boxed{
V_Y=\#\{i:T_i\subset Q\}.
}
\tag{5.4}
\]
The number of literal central rank-seven five-windows with color \(Q\) is
exactly
\[
\boxed{W_Y.}
\tag{5.5}
\]
Furthermore,
\[
\boxed{
0\leq V_Y\leq7,
}
\tag{5.6}
\]
\[
\boxed{
V_Y=W_Y+b_Y+u_{4,Y}.
}
\tag{5.7}
\]
Consequently,
\[
\boxed{
W_Y+b_Y\leq7,\qquad
W_Y\leq6,\qquad
b_Y\leq3.
}
\tag{5.8}
\]
Equivalently, if the long run lengths are
\(\ell_1,\ldots,\ell_{b_Y}\geq5\), then
\[
\boxed{
\sum_{j=1}^{b_Y}(\ell_j-3)\leq7.
}
\tag{5.9}
\]

#### Proof

A run of length \(\ell\) contains \((\ell-3)_+\) length-four
subwindows and \((\ell-4)_+\) length-five subwindows. A four-window is
\(Y\)-free exactly when its rank-six OR \(T_i\) is contained in
\(Q\), proving (5.4).

Put
\[
D_i=\Omega\setminus T_i.
\]
The \(D_i\) are distinct five-sets. The condition \(T_i\subset Q\) is
equivalent to \(Y\subset D_i\). There are exactly seven five-set supersets
of \(Y\), proving \(V_Y\leq7\).

A \(Y\)-free central five-window has OR contained in \(Q\). Every ordinary
five-window has rank seven and must therefore equal \(Q\). When
\(\eta=0\), the seam window also has rank seven and is counted in exactly
the same way. When \(\eta>0\), it has rank greater than seven and cannot be
contained in \(Q\). This proves (5.5).

Every run of length at least five contributes one more length-four window
than length-five windows, and every exact length-four run contributes one
length-four window. This gives (5.7). Equations (5.8)--(5.9) follow.
\(\square\)

### Corollary 5.2: an eleven-cell rank theorem

No four coordinates are simultaneously absent from eleven consecutive
central entries. Equivalently, every eleven-entry central interval has OR
rank at least eight:
\[
\boxed{
\left|
\bigcup_{j=i}^{i+10}A_j
\right|\geq8.
}
\tag{5.10}
\]

Indeed, a joint \(Y\)-zero-run of length eleven would give
\[
V_Y\geq11-3=8,
\]
contrary to (5.6).

### Theorem 5.3: local folds and separated returns

For \(b_Y>0\), define
\[
\mathcal A_Y=W_Y-b_Y
=\sum_{\ell}(\ell-5)_+,
\tag{5.11}
\]
\[
\mathcal S_Y=b_Y-1.
\tag{5.12}
\]
Then
\[
\boxed{
W_Y-1=\mathcal A_Y+\mathcal S_Y,
}
\tag{5.13}
\]
and
\[
\boxed{
\mathcal A_Y+2\mathcal S_Y+u_{4,Y}
=V_Y-2
\leq5.
}
\tag{5.14}
\]

Here \(\mathcal A_Y\) is the number of adjacent equal literal central
\(Q\)-windows, while \(\mathcal S_Y\) is the number of separated
reappearances.

Distinct \(Q\)-blocks have initial five-window indices differing by at
least six. In particular, there are at least five intervening non-\(Q\)
five-window positions.

#### Proof

A run of \(\ell\geq5\) gives \(\ell-4\) consecutive \(Q\)-windows and
therefore \(\ell-5\) adjacent equalities. Different long zero-runs give the
separated blocks. Equations (5.13)--(5.14) follow from (5.7).

Between two maximal \(Y\)-zero-runs there is an entry meeting \(Y\). The
last \(Q\)-window of the first run starts four positions before that run
ends, while the first \(Q\)-window of the next run begins after the
intervening nonzero entry. Their start difference is at least six.
\(\square\)

An adjacent equality also has an exact one-coordinate restitution. If
two consecutive central five-windows equal \(Q\) and their common
four-window is \(T_i\), then
\[
x=Q\setminus T_i
\tag{5.15}
\]
is present in both flanking entries and absent from the four entries of
\(T_i\). It is an exact length-four \(x\)-zero-run. Along the oriented
six-path, provided both adjacent transitions survive the state and seam
cuts, it is the incoming deletion followed by the outgoing matching gain.
A literal fold involving the removed seam transition is not a postcut lazy
turn.

### Theorem 5.4: missing-facet normal form inside one central block

Suppose
\[
T_a,T_{a+1},\ldots,T_{a+r}
\]
are consecutive distinct facets of one seven-set \(Q\). Write
\[
T_j=Q\setminus\{\theta_j\}.
\tag{5.16}
\]
Then the \(\theta_j\)'s are distinct. Away from the exceptional seam,
\[
C_j
=Q\setminus\{\theta_{j-1},\theta_j\}.
\tag{5.17}
\]
Here (5.17) is asserted for
\[
a+1\leq j\leq a+r,\qquad C_j\neq H.
\]
For
\[
a+2\leq j\leq a+r,
\]
whenever \(C_{j-1},C_j\) and the pair color
\[
P_j:=A_j\cup A_{j+1}
\]
are ordinary,
\[
P_j
=Q\setminus
\{\theta_{j-2},\theta_{j-1},\theta_j\}.
\tag{5.18}
\]
For \(a+3\leq j\leq a+r\), whenever the two relevant pair formulas
apply and \(|A_j|=3\),
\[
A_j
=Q\setminus
\{\theta_{j-3},\theta_{j-2},
\theta_{j-1},\theta_j\}.
\tag{5.19}
\]

Thus an extremal six-edge \(Q\)-block is locally compatible with
rank-three entries. The bound \(W_Y\leq6\) cannot be improved from
rank-at-most-three geometry alone.

#### Proof

Distinct \(T_j\)'s are distinct facets of \(Q\), so the missing coordinates
are distinct. Consecutive ordinary facets intersect in the ordinary
five-set \(C_j\), giving (5.17). Intersecting two consecutive ordinary
\(C\)'s gives the ordinary rank-four pair \(P_j\), proving (5.18).
Intersecting the relevant consecutive rank-four pairs gives a three-set;
if \(A_j\) has rank three, containment becomes equality, proving (5.19).
\(\square\)

Sharpness is literal and is compatible with distinct ordinary pair and
triple colors. Write \(Q=\{\theta_0,\ldots,\theta_6\}\) and take the ten
rank-three entries
\[
\begin{array}{lll}
A_0=123,&A_1=234,&A_2=345,\\
A_3=456,&A_4=560,&A_5=601,\\
A_6=012,&A_7=023,&A_8=024,\\
&&A_9=025,
\end{array}
\tag{5.20}
\]
where, for example, \(123=\{\theta_1,\theta_2,\theta_3\}\). Direct union
gives, for \(0\leq i\leq6\),
\[
T_i=Q\setminus\{\theta_i\}.
\]
The nine pair colors are
\[
1234,\ 2345,\ 3456,\ 0456,\ 0156,\ 0126,\ 0123,\ 0234,\ 0245,
\]
and the eight triple colors are
\[
12345,\ 23456,\ 03456,\ 01456,\ 01256,\ 01236,\ 01234,\ 02345.
\]
They are respectively distinct rank-four and distinct rank-five colors.
The first six facet transitions all have union \(Q\), giving a literal
local realization of multiplicity six in the full ordinary
rank-four/rank-five/rank-six normal form.

### Seam correction

If the seam is internal with \(\eta=0\), let \(Y_*\) be the complement of
the seam-centered rank-seven five-window. The central-core forest
multiplicity is
\[
c_Y=W_Y-\mathbf1_{\{Y=Y_*\}}.
\tag{5.21}
\]
In every other seam case,
\[
c_Y=W_Y.
\tag{5.22}
\]
The removed seam edge is not part of the postcut central forest even when
its literal five-window has rank seven.

For exact duplicate bookkeeping in the internal \(\eta=0\) case, put
\[
z_{\rm lit}=\#\{Y:W_Y>0\},
\qquad
\Delta_{\rm lit}=\sum_Y(W_Y-1)_+.
\]
Define the corresponding postcut quantities by
\[
z_C=\#\{Y:c_Y>0\},
\qquad
\Delta_C=\sum_Y(c_Y-1)_+.
\]
Then
\[
\boxed{
z_C=z_{\rm lit}-\mathbf1_{\{W_{Y_*}=1\}},
\qquad
\Delta_C=\Delta_{\rm lit}-\mathbf1_{\{W_{Y_*}\geq2\}}.
}
\tag{5.23}
\]
Put
\[
\lambda_-=\mathbf1_{\{\mathscr Q_{s-2}=Q_*\}},
\qquad
\lambda_+=\mathbf1_{\{\mathscr Q_s=Q_*\}},
\]
where \(Q_*=\Omega\setminus Y_*\) and \(\mathscr Q_j\) denotes the literal
five-window color at start \(j\). An indicator is defined to be zero when
its neighboring index is outside the five-window range. Removing the seam
occurrence deletes
\(\lambda_-+\lambda_+\) literal adjacent equalities. If both indicators
are one, a literal block splits into two postcut components: the lazy
count drops by two and the separated-return count rises by one.

### Theorem 5.5: endpoint-charged central support

Let
\[
\varepsilon_*=
\mathbf1_{\{\text{internal seam},\ \eta=0,\ W_{Y_*}=1\}}.
\tag{5.24}
\]
Put
\[
\mathcal Y_0=\{Y\in\binom{\Omega}{4}:c_Y=0\}.
\]
Then
\[
\boxed{
z_{\rm lit}\geq m-135=330-E,
}
\tag{5.25}
\]
and therefore
\[
\boxed{
z_C\geq m-135-\varepsilon_*,
\qquad
|\mathcal Y_0|\leq E+\varepsilon_*\leq E+1.
}
\tag{5.26}
\]
The postcut central duplicate excess also obeys
\[
\boxed{
\Delta_C\leq132-b_H+\varepsilon_*\leq131.
}
\tag{5.27}
\]
More precisely, the upper bound is \(130\) for an internal
\(\eta>0\) seam and is at most \(131\) in the other seam cases.

#### Proof

Choose one literal witness for every rank-seven target. A rank-seven
witness wholly inside the central segment has at least five entries,
because every central interval of at most four entries is contained in a
rank-six four-window. It therefore contains a central five-window. That
five-window has rank at least seven and is contained in the rank-seven
target, so it has exactly that target color.

Consequently, a target absent from the literal central support has a
selected witness extending outside \([L,R]\). Charge it to its left
endpoint before \(L\), if it has one, and otherwise to its right endpoint
after \(R\). Selected witnesses of distinct rank-seven targets have
distinct left endpoints and distinct right endpoints. There are exactly
\[
L+(464-R)=465-m=E
\]
available external endpoint positions. Thus at most \(E\) targets are
absent from the literal central support, proving (5.25).

Equation (5.23) gives the support loss \(\varepsilon_*\), proving (5.26).
Finally,
\[
\Delta_C=N_C-z_C
\leq(m-3-b_H)-(m-135-\varepsilon_*)
=132-b_H+\varepsilon_*.
\]
If the seam is internal then \(b_H=2\); if it is an endpoint seam then
\(b_H=1\) and \(\varepsilon_*=0\). This proves (5.27).
\(\square\)

## 6. Exact interfaces and the central/outer split

The left-oriented states \(00,01,02\) point in increasing endpoint order.
The right-oriented states \(13,23,33\) point in decreasing endpoint order.
Consequently every retained external/central interface points from an
external six-set into a central six-set.

Let
\[
0\leq d\leq b_H
\tag{6.1}
\]
be the number of retained interfaces. Then:

\[
\boxed{
N_C=q-b_H=m-3-b_H
}
\tag{6.2}
\]
is the number of internal central-core hulls;

\[
\boxed{
N_O=E+b_H-c
}
\tag{6.3}
\]
is the number of all remaining outer hulls;

\[
\boxed{
R_{\rm ext}=E+b_H-c-d
}
\tag{6.4}
\]
is the number of external-headed hulls;

\[
\boxed{
s_{\rm ext}=c-b_H+d
}
\tag{6.5}
\]
is the number of external-start components.

In particular,
\[
\boxed{
R_{\rm ext}\geq E-c\geq126.
}
\tag{6.6}
\]

#### Proof

The \(q\) central six-set vertices form \(b_H\) internal path pieces, giving
\(q-b_H\) central-central edges. Each retained interface joins an external
predecessor to the initial vertex of one such piece.

Exactly \(b_H-d\) central pieces remain component starts. Thus the other
\[
c-(b_H-d)=c-b_H+d
\]
component starts are external. Every external six-set except those starts
has an incoming edge, and an external-headed edge has an external
predecessor. Hence (6.4)--(6.5). Equation (6.3) is either the remaining
edge count or \(d+R_{\rm ext}\). Finally \(E\geq132\) and \(c\leq6\).
\(\square\)

For each \(Y\), let \(\rho_Y\) be the number of interface hulls with
rank-seven complement \(Y\). Then
\[
\sum_Y\rho_Y=d.
\tag{6.7}
\]
Let \(x_Y\) be the external-headed multiplicity of
\(Q=\Omega\setminus Y\).

### Theorem 6.1: exact central/external facet coupling

\[
\boxed{
0\leq x_Y\leq(6-V_Y)_+.
}
\tag{6.8}
\]
The complete global multiplicity is
\[
\boxed{
t_{\Omega\setminus Y}
=c_Y+\rho_Y+x_Y.
}
\tag{6.9}
\]
Also,
\[
\sum_Yx_Y=R_{\rm ext},
\qquad
\sum_Yc_Y=N_C.
\tag{6.10}
\]

#### Proof

The seven six-facets of \(Q\) correspond, after complementation, to the
seven five-set supersets of \(Y\). Exactly \(V_Y\) of those facets are
central \(T_i\)'s. An external-headed \(Q\)-edge has two external facets.
The external \(Q\)-edges form a linear forest on the remaining
\(7-V_Y\) vertices, and hence have at most
\((7-V_Y)-1=6-V_Y\) edges when that number is positive. This proves
(6.8). The three disjoint edge classes give (6.9)--(6.10).
\(\square\)

The aggregate external-facet capacity is exactly
\[
\boxed{
\sum_Y(6-V_Y)_+
=5E-330+N_7^\star,
}
\tag{6.11}
\]
where
\[
N_7^\star=\#\{Y:V_Y=7\}.
\tag{6.12}
\]
Indeed,
\[
\sum_YV_Y=5q,
\]
because every central six-set facet belongs to five seven-sets, and
\[
(6-v)_+=6-v+\mathbf1_{\{v=7\}}.
\]
At \(E\geq132\), (6.11) is at least \(330\), while only at most \(E\)
external-headed arcs are required. Thus the scalar sum has large slack.

### Corollary 6.2: high-star colors

\[
\boxed{
\#\{Y:c_Y=0,\ V_Y\geq6\}
\leq M_7+d
\leq13.
}
\tag{6.13}
\]

More precisely:

* if \(c_Y=0\) and \(V_Y=7\), then \(Q\) is globally missing;
* if \(c_Y=0,V_Y=6\), and \(Q\) is present, its only possible support is
  an interface.

Furthermore, colors with
\[
V_Y\geq5,\qquad c_Y=0
\]
contribute at most \(d\) total duplicate excess. Hence at least
\[
\boxed{126-d\geq124}
\tag{6.14}
\]
units of duplicate excess lie on colors satisfying
\[
c_Y>0\quad\text{or}\quad V_Y\leq4.
\]

#### Proof

For \(V_Y=7\), no external facet remains and neither an external-headed nor
an interface edge is possible. For \(V_Y=6\), only one external facet
remains, so no external-external edge is possible; one interface can use
it.

If \(V_Y=5\), the external-headed capacity is one. Without an interface,
such a centrally inactive color cannot repeat. Every duplicate unit in the
stated inactive high-star class therefore consumes an interface, and there
are only \(d\).
\(\square\)

## 7. External directed complement flags

Put
\[
\mathcal P_{\rm ext}=[0,L-1]\cup[R+1,464].
\]
Endpoint saturation gives, for every \(p\in\mathcal P_{\rm ext}\), a
matched pair of selected witnesses \(I_p\subsetneq J_p\): their common
left endpoint is \(p\) on the prefix and their common right endpoint is
\(p\) on the suffix. Write
\[
S_p=\operatorname{OR}(I_p),\qquad
U_p=\operatorname{OR}(J_p),\qquad
\xi_p=U_p\setminus S_p.
\]
Let \(\mathcal P_{\rm h}\subseteq\mathcal P_{\rm ext}\) be the anchors
whose six-set is the destination of an external-headed forest arc. Then
\[
|\mathcal P_{\rm h}|=R_{\rm ext}.
\]
For \(p\in\mathcal P_{\rm h}\), the adjacent predecessor anchor toward the
outer end is
\[
p^-=
\begin{cases}
p-1,&p<L,\\
p+1,&p>R.
\end{cases}
\]
Both anchors are in the same offset-state block, and the intervening
matching source gives
\[
\operatorname{OR}(I_p)=M^{-1}(U_p)=U_{p^-}\cap U_p.
\]
Thus, consistently with this notation, write
\[
S_p=U_{p^-}\cap U_p,
\tag{7.1}
\]
\[
\xi_p=U_p\setminus S_p,
\qquad
\beta_p=U_{p^-}\setminus S_p.
\tag{7.2}
\]
Thus
\[
Q_p=U_{p^-}\cup U_p
=S_p\sqcup\{\xi_p,\beta_p\}.
\tag{7.3}
\]
Put
\[
Y_p=\Omega\setminus Q_p,
\qquad
\widehat C_p=\Omega\setminus S_p,
\qquad
\widehat D_p=\Omega\setminus U_p,
\qquad
\widehat D'_p=\Omega\setminus U_{p^-}.
\tag{7.4}
\]

### Theorem 7.1: exact depth-two complement flag

\[
\boxed{
Y_p\subset\widehat D_p,\widehat D'_p
\subset\widehat C_p,
}
\tag{7.5}
\]
and
\[
\boxed{
\widehat C_p
=Y_p\sqcup\{\xi_p,\beta_p\},
}
\tag{7.6}
\]
\[
\boxed{
\widehat D_p=Y_p\sqcup\{\beta_p\},
\qquad
\widehat D'_p=Y_p\sqcup\{\xi_p\}.
}
\tag{7.7}
\]
For a fixed \(Q\), the arrows
\[
\xi_p\longrightarrow\beta_p
\tag{7.8}
\]
form a directed linear forest on \(Q\). In particular, the \(\xi_p\)'s are
pairwise distinct and the \(\beta_p\)'s are pairwise distinct among the
\(Q\)-colored external-headed edges.

#### Proof

Equations (7.5)--(7.7) are complements of
\[
S_p\subset U_p,U_{p^-}\subset Q_p.
\]
Under the missing-coordinate identification of the six-facets of \(Q\),
the predecessor is \(Q\setminus\{\xi_p\}\), while the destination is
\(Q\setminus\{\beta_p\}\). Thus the edge is
\(\xi_p\to\beta_p\). The ambient six-forest has indegree and outdegree at
most one and no cycle, proving the last assertion.
\(\square\)

Let \(I_p\) and \(J_p\) be the matched physical source and destination
witnesses. The anchor entry \(B_p\) belongs to \(I_p\), and
\[
B_p\subseteq S_p.
\tag{7.9}
\]

### Theorem 7.2: two-label physical exposure

Both coordinates \(\xi_p,\beta_p\) are absent from every entry of \(I_p\).
The coordinate \(\xi_p\) occurs in \(J_p\setminus I_p\), while
\(\beta_p\) occurs in \(J_{p^-}\setminus I_p\).

For a prefix anchor, their possible occurrence offsets from \(p\) are
contained in
\[
\{-1,+1,+2,+3\}.
\tag{7.10}
\]
More precisely,
\[
\xi_p:\{+1,+2,+3\},
\qquad
\beta_p:\{-1,+1,+2\}.
\]
For a suffix anchor, they are contained in
\[
\{+1,-1,-2,-3\}.
\tag{7.11}
\]
The two displayed prefix offset sets reverse on the suffix.

#### Proof

The pair is \(Q_p\setminus S_p\), and
\(\operatorname{OR}(I_p)=S_p\), so neither coordinate occurs anywhere in
\(I_p\). Since
\[
\xi_p\in U_p\setminus S_p,\qquad
\beta_p\in U_{p^-}\setminus S_p,
\]
the first has an occurrence in \(J_p\setminus I_p\), and the second has
an occurrence in \(J_{p^-}\setminus I_p\).

On the prefix, \(I_p,J_p\) start at \(p\), while the predecessor
\(J_{p^-}\) starts at \(p-1\). All selected rank-six witnesses have at
most four physical cells. The destination difference lies at
\(p+1,p+2,p+3\). The predecessor difference can use \(p-1\) and, depending
on the source length, \(p+1,p+2\). This gives (7.10). The suffix is the
reversal.
\(\square\)

Let
\[
\mathcal H_{\rm ext}
=[0,L+2]\cup[R-2,464]
\tag{7.12}
\]
be the external halo. For \(X\subseteq\Omega\), define
\[
P_X
=\#\{p\in\mathcal P_{\rm h}:
\{\xi_p,\beta_p\}\cap X\neq\varnothing\},
\tag{7.13}
\]
\[
\widetilde P_X
=\sum_{p\in\mathcal P_{\rm h}}
|\{\xi_p,\beta_p\}\cap X|,
\tag{7.14}
\]
\[
u_X
=\#\{t\in\mathcal H_{\rm ext}:B_t\cap X\neq\varnothing\},
\tag{7.15}
\]
\[
\widetilde u_X
=\sum_{t\in\mathcal H_{\rm ext}}|B_t\cap X|.
\tag{7.16}
\]

### Corollary 7.3: factor-four pair capacity

\[
\boxed{P_X\leq4u_X,}
\tag{7.17}
\]
\[
\boxed{\widetilde P_X\leq4\widetilde u_X.}
\tag{7.18}
\]

#### Proof

Choose one physical occurrence for a pair meeting \(X\), or one occurrence
for each member of the pair lying in \(X\). By (7.10)--(7.11), a fixed
halo position can be reached from at most four external-headed anchors.
The classified central segment has \(m\geq228\), so the prefix and suffix
halos are disjoint and their charges cannot accumulate.
For the weighted assertion, charge a coordinate occurrence \((t,x)\);
each such pair is reached from at most four anchors.
\(\square\)

The factor four in (7.17) is unweighted and counts pair-meeting. Equation
(7.18) requires the weighted halo incidence. In general it would be false
to replace \(\widetilde u_X\) by \(u_X\), since one word entry may contain
both pair coordinates.

## 8. Nested Hall systems

### 8.1 The simple head-label matrix

For every global rank-seven color \(Q\) and coordinate \(x\), let
\[
L_{Qx}
\]
count \(Q\)-colored forest arcs whose destination matching label is \(x\).

### Theorem 8.1: global simple matrix

\[
\boxed{
L_{Qx}\in\{0,1\},\qquad
L_{Qx}=0\text{ if }x\notin Q.
}
\tag{8.1}
\]
Its margins are
\[
\boxed{
\sum_xL_{Qx}=t_Q,
\qquad
\sum_QL_{Qx}=42-\pi_x.
}
\tag{8.2}
\]

#### Proof

A \(Q\)-arc with head label \(x\) has predecessor facet
\(Q\setminus\{x\}\). Two such arcs would have the same predecessor and
violate outdegree one. This proves simplicity. The row sum counts the
\(Q\)-edges. Every matching label except a component-start label is the
head label of one six-path edge, proving the column sum.
\(\square\)

For a coordinate \(x\), let
\[
R_x^{(3)}
=\#\{\text{maximal central \(x\)-zero-runs of length at least three}\},
\]
and let
\[
e_x^{\rm ext}
=\#\{p\in\mathcal P_{\rm ext}:\xi_p=x\}.
\]
The audited external label split gives
\[
e_x^{\rm ext}
=43-R_x^{(3)}-\mathbf1_{\{x\in H\}},
\qquad
\sum_xe_x^{\rm ext}=E.
\]
Let \(\iota_x\) count external-start matching labels. Then
\[
\sum_x\iota_x=s_{\rm ext}.
\tag{8.3}
\]
The number of external-headed arcs with matching label \(x\) is
\[
\omega_x
=e_x^{\rm ext}-\iota_x
=43-R_x^{(3)}-\mathbf1_{\{x\in H\}}-\iota_x.
\tag{8.4}
\]
In particular,
\[
\boxed{
\sum_x\omega_x
=E-s_{\rm ext}
=R_{\rm ext}
=\sum_Qx_{\Omega\setminus Q}.
}
\tag{8.4a}
\]

For \(Q\), let \(\Lambda_Q^{\rm cen}\subset Q\) be the set of head labels
already used on its central-core and interface arcs. Put
\[
\mathcal A_Q=Q\setminus\Lambda_Q^{\rm cen}.
\tag{8.5}
\]

### Theorem 8.2: exact projected head-label Hall criterion

There is a zero-one matrix \(y_{Qx}\) satisfying
\[
y_{Qx}=0\quad(x\notin\mathcal A_Q),
\tag{8.6}
\]
\[
\sum_xy_{Qx}=x_{\Omega\setminus Q},
\qquad
\sum_Qy_{Qx}=\omega_x.
\tag{8.7}
\]
Equivalently, for every \(X\subseteq\Omega\),
\[
\boxed{
\sum_Q
\left(
x_{\Omega\setminus Q}
-|\mathcal A_Q\setminus X|
\right)_+
\leq
\sum_{x\in X}\omega_x.
}
\tag{8.8}
\]

#### Proof

Restrict the actual global simple matrix to the external-headed arcs. Its
row and column margins are (8.7), and simplicity forbids reuse of the
central labels, proving existence.

Conversely, make a flow network with source-to-row capacity
\(x_{\Omega\setminus Q}\), unit-capacity edges \(Q\to x\) for
\(x\in\mathcal A_Q\), and coordinate-to-sink capacity \(\omega_x\).
A cut with coordinate set \(X\) forces at least
\[
\left(x_{\Omega\setminus Q}-|\mathcal A_Q\setminus X|\right)_+
\]
units of row \(Q\) through \(X\). The max-flow/min-cut theorem and the
equal totals (8.4a) give (8.8), and these cuts are sufficient for the
projected matrix. All capacities are integral, so an integral maximum flow
gives a zero-one matrix.
\(\square\)

This is an exact theorem for the coordinate-label projection. It is not
sufficient for the physical predecessor order.

### 8.2 Head-restricted external-offset Hall

For later comparison, define the full-anchor quantities
\[
\begin{aligned}
e^{\rm ext}(X)
&=\#\{p\in\mathcal P_{\rm ext}:\xi_p\in X\},\\
s_X
&=\#\{p\in\mathcal P_{\rm ext}:X\subseteq S_p\},\\
a_X
&=\#\{p\in\mathcal P_{\rm ext}:X\subseteq B_p\},\\
d_X
&=\#\{p\in\mathcal P_{\rm ext}:
\operatorname{OR}(J_p\setminus I_p)\cap X\neq\varnothing\}.
\end{aligned}
\tag{8.8a}
\]
The external-offset theorem and its independent audit,
K11_EXTERNAL_OFFSET_CAPACITY_20260724.md and
K11_EXTERNAL_OFFSET_CAPACITY_AUDIT_20260724.md, give
\[
\boxed{
e^{\rm ext}(X)
\leq\min\{E-s_X,E-a_X,d_X\}
\leq3u_X.
}
\tag{8.8b}
\]

Among the \(R_{\rm ext}\) external-headed anchors, define
\[
s_X^{\rm h}
=\#\{p\in\mathcal P_{\rm h}:X\subseteq S_p\},
\tag{8.9}
\]
\[
a_X^{\rm h}
=\#\{p\in\mathcal P_{\rm h}:X\subseteq B_p\},
\tag{8.10}
\]
\[
d_X^{\rm h}
=\#\{p\in\mathcal P_{\rm h}:
\operatorname{OR}(J_p\setminus I_p)\cap X
\neq\varnothing\}.
\tag{8.11}
\]

### Theorem 8.3: nested head-label Hall

Let
\[
\omega(X)=\sum_{x\in X}\omega_x.
\]
Then
\[
\boxed{
\sum_Q
\left(
x_{\Omega\setminus Q}
-|\mathcal A_Q\setminus X|
\right)_+
\leq\omega(X)
\leq
\min\{
R_{\rm ext}-s_X^{\rm h},
R_{\rm ext}-a_X^{\rm h},
d_X^{\rm h}
\}
\leq3u_X.
}
\tag{8.12}
\]

#### Proof

The left inequality is (8.8). If a head label belongs to \(X\), its
rank-five source and anchor entry cannot contain all of \(X\), because
that label is absent from both. The label occurs in the directed
destination added block. This proves the three middle capacities. The
same three-offset charge used in the audited external-offset theorem gives
the final factor three.
\(\square\)

For any family \(\mathcal F\) of rank-seven colors, with
\[
X=\bigcup_{Q\in\mathcal F}Q,
\]
one immediate, usually coarse corollary is
\[
\boxed{
\sum_{Q\in\mathcal F}x_{\Omega\setminus Q}
\leq e^{\rm ext}(X)
\leq\min\{E-s_X,E-a_X,d_X\}
\leq3u_X.
}
\tag{8.13}
\]

### 8.3 Full-pair Hall

For a rank-seven set \(Q\), put
\[
\mathcal E_Q
=\{z\in Q:Q\setminus\{z\}
\text{ is an external six-set}\}.
\tag{8.14}
\]
Then
\[
|\mathcal E_Q|=7-V_{\Omega\setminus Q}.
\tag{8.15}
\]
The external-headed \(Q\)-arcs form a linear forest on
\(\mathcal E_Q\).

For \(X\subseteq\Omega\), set
\[
s_Q(X)=|\mathcal E_Q\setminus X|.
\tag{8.16}
\]

### Theorem 8.4: pair-meeting Hall

\[
\boxed{
\sum_Q
\left[
x_{\Omega\setminus Q}
-(s_Q(X)-1)_+
\right]_+
\leq P_X
\leq
\min\{
R_{\rm ext}-s_X^{\rm h},
R_{\rm ext}-a_X^{\rm h},
4u_X
\}.
}
\tag{8.17}
\]

For weighted pair incidence define
\[
\phi(r,s)=
\begin{cases}
0,&r\leq s-1,\\
1,&r=s>0,\\
2(r-s),&r\geq s+1,
\end{cases}
\qquad
\phi(0,0)=0.
\tag{8.18}
\]
Then
\[
\boxed{
\sum_Q\phi(x_{\Omega\setminus Q},s_Q(X))
\leq\widetilde P_X
\leq4\widetilde u_X.
}
\tag{8.19}
\]

#### Proof

A forest on \(s\) vertices outside \(X\) has at most \((s-1)_+\) edges
whose two endpoints avoid \(X\). This proves the lower bound in (8.17).
The source, anchor, and physical factor-four arguments prove the upper
bound.

For one \(Q\)-forest with \(r\) edges and \(s\) vertices outside \(X\),
its weighted \(X\)-incidence is
\[
2r-\sum_{v\in\mathcal E_Q\setminus X}\deg(v).
\]
If \(r\leq s-1\), the trivial lower bound is zero. If \(r=s>0\), zero
incidence would require \(r=s\) forest edges on only \(s\) outside
vertices, impossible. If \(r\geq s+1\), the outside degree sum is at most
\(2s\), giving \(2(r-s)\). These are precisely the three cases in
(8.18). Summing over \(Q\) and applying (7.18) proves (8.19).
\(\square\)

Equation (8.8) is an exact if-and-only-if criterion for the projected
simple head-label matrix. The nested offset inequalities (8.12), pair
inequalities (8.17)--(8.19), and complement-star inequalities below are
necessary physical or anchor projections only; they are not sufficient
for the two-label tensor or the word. Full realization also requires
distinct destination labels, acyclicity, literal anchor containment, and,
at each anchor, the fixed predecessor equation
\[
U_{p^-}=Q_p\setminus\{\xi_p\}
\tag{8.20}
\]
in the fixed predecessor order.

## 9. Complement-star support Hall

Recall
\[
\mathcal Y_0=\{Y\in\binom{\Omega}{4}:c_Y=0\}.
\tag{9.1}
\]
For \(Z\subseteq\Omega\), \(|Z|\leq4\), define
\[
N_Z^0
=\#\{Y\in\mathcal Y_0:Z\subseteq Y\}.
\tag{9.2}
\]
Define
\[
M_Z^\perp
=\#\{Y\in\mathcal Y_0:
Z\subseteq Y,\ t_{\Omega\setminus Y}=0\},
\]
\[
I_Z
=\#\{Y\in\mathcal Y_0:
Z\subseteq Y,\ \rho_Y>0\},
\]
and put
\[
o_Z^{\rm ext}
=\#\{p\in\mathcal P_{\rm h}:B_p\cap Z=\varnothing\}.
\tag{9.3}
\]

### Theorem 9.1: complement-star Hall cut

\[
\boxed{
N_Z^0-M_Z^\perp-I_Z
\leq o_Z^{\rm ext},
\qquad
I_Z\leq d.
}
\tag{9.4}
\]

Let
\[
\omega_Z^{\rm cen}
=\sum_{\substack{Y\supseteq Z\\|Y|=4}}c_Y;
\]
this is the number of internal central-core five-window occurrences whose
OR avoids \(Z\). Then
\[
\boxed{
\binom{11-|Z|}{4-|Z|}
-\omega_Z^{\rm cen}
\leq
M_Z^\perp+I_Z+o_Z^{\rm ext}
\leq
M_Z^\perp+d+o_Z^{\rm ext}.
}
\tag{9.5}
\]

#### Proof

Every \(Y\in\mathcal Y_0\) whose complement is globally present must be
represented either by an interface or by an external-headed hull. After
choosing one occurrence per color, distinct colors use distinct hull
anchors. If \(Z\subseteq Y\), every entry of that hull, and in particular
its anchor entry, avoids \(Z\). This proves (9.4).

There are
\[
\binom{11-|Z|}{4-|Z|}
\]
four-sets containing \(Z\). Every one whose complement occurs in the
central core contributes at least one central five-window avoiding \(Z\).
The number of such distinct colors is at most the occurrence count
\(\omega_Z^{\rm cen}\), giving the lower bound on \(N_Z^0\) and hence
(9.5).
\(\square\)

For \(Z=\{x\}\), let \(a_x\) be the total number of external anchors whose
entry contains \(x\), and let \(s_{0,x}^{\rm omit}\) count external-start
anchors omitting \(x\). Then
\[
o_{\{x\}}^{\rm ext}
=E-a_x-s_{0,x}^{\rm omit},
\]
so
\[
\boxed{
120-\omega_x^{\rm cen}
\leq
M_x^\perp+I_x
+E-a_x-s_{0,x}^{\rm omit}.
}
\tag{9.6}
\]
Here \(M_x^\perp:=M_{\{x\}}^\perp\),
\(I_x:=I_{\{x\}}\), and
\(\omega_x^{\rm cen}:=\omega_{\{x\}}^{\rm cen}\).
This is the cleanest direct coupling between the low-entry joint-zero
geometry and the external anchor family.

## 10. Endpoint widths and physical spread

The following section combines the physical hulls with the audited
three-layer truncated-width theorem.

For the rank-six row write
\[
u_j=j+\lambda_j,\qquad
v_j=j+\rho_j,
\qquad
0\leq\lambda_j\leq\rho_j\leq3.
\tag{10.1}
\]
The two offset sequences \((\lambda_j)\) and \((\rho_j)\) are
nondecreasing. Choose one rank-seven witness for every target, and let
\(e_L,e_R\leq3\) count the targets whose selected left, respectively
right, endpoint is not shared by the rank-six row. Let
\[
p\geq330-e_L-e_R\geq324
\]
be the number of selected rank-seven witnesses sharing both endpoints with
the rank-six row. For such a target \(Q\), let
\(i_Q^{\rm L},i_Q^{\rm R}\) be its common-left and common-right rank-six
indices. Put
\[
1\leq g_Q:=i_Q^{\rm R}-i_Q^{\rm L}\leq6,
\tag{10.2}
\]
\[
\delta_Q:=\rho_{i_Q^{\rm R}}-\lambda_{i_Q^{\rm L}}.
\]
Its exact selected physical width is
\[
\boxed{
w_Q=g_Q+\delta_Q.
}
\tag{10.3}
\]
The crossed spans have disjoint gap sets, so
\[
\sum_{\rm crossed}g_Q\leq461.
\tag{10.4}
\]

Let \(\mathcal T_7\) be the sum of the selected rank-seven widths truncated
at four. Type I is the frozen branch with one selected rank-six singleton,
and Type II is the branch with none. The audited bounds hold for every
one-witness-per-rank-seven-target selection with the fixed canonical
rank-five/rank-six rows:
\[
\mathcal T_7\geq930
\quad\text{in Type II},
\qquad
\mathcal T_7\geq940
\quad\text{in Type I}.
\tag{10.5}
\]

### Theorem 10.1: crossed offset-spread mass

In Type II,
\[
\boxed{
\sum_{\rm crossed}
\delta_Q
\geq4p-851
\geq445.
}
\tag{10.6}
\]
In Type I,
\[
\boxed{
\sum_{\rm crossed}
\delta_Q
\geq4p-841
\geq455.
}
\tag{10.7}
\]

Consequently at least \(61\) Type-II crossed targets, and at least \(66\)
Type-I crossed targets, have
\[
\delta_Q\geq2.
\tag{10.8}
\]

#### Proof

The \(330-p\) noncrossed targets contribute at most four each to
\(\mathcal T_7\). Therefore
\[
\sum_{\rm crossed}\min(w_Q,4)
\geq\mathcal T_7-4(330-p).
\]
Since \(\min(w_Q,4)\leq w_Q\), equations
(10.3)--(10.4) give
\[
\sum_{\rm crossed}\delta_Q
\geq
\mathcal T_7-4(330-p)-461.
\]
Substitute (10.5).

Every offset spread is at most three. If \(h\) terms have spread at least
two and the other \(p-h\) have spread at most one, the sum is at most
\[
3h+(p-h)=p+2h.
\]
Using \(p\geq324\) in (10.6)--(10.7) gives \(h\geq61,66\).
\(\square\)

### Theorem 10.2: minimum-hull width deficit

For every supported rank-seven color \(Q\), choose a physical forest hull
of minimum width \(\widehat w_Q\). Then
\[
2\leq\widehat w_Q\leq4.
\]
In Type II,
\[
\boxed{
\sum_{Q:t_Q>0}(4-\widehat w_Q)\leq390.
}
\tag{10.9}
\]
In Type I,
\[
\boxed{
\sum_{Q:t_Q>0}(4-\widehat w_Q)\leq380.
}
\tag{10.10}
\]

#### Proof

Use the chosen minimum hull as the witness for every supported color and
choose arbitrary witnesses for the \(M_7\) missing colors. The latter
contribute at most \(4M_7\) to the truncated sum. Hence
\[
\sum_{Q:t_Q>0}\widehat w_Q+4M_7
\geq\mathcal T_7.
\]
This reselection is legitimate because the audited bound (10.5) holds for
every one-witness-per-target rank-seven selection with the fixed lower
rows.
Since the support size is \(330-M_7\), rearrangement gives
\[
\sum_{Q:t_Q>0}(4-\widehat w_Q)
\leq1320-\mathcal T_7.
\]
Apply (10.5).
\(\square\)

Neither offset-spread theorem is contradictory: the maximum available
spread is \(3p\), and the deficit bounds retain hundreds of units of
slack.

## 11. Duplicate pressure after the physical lift

The exact full multiplicity formula is
\[
t_{\Omega\setminus Y}=c_Y+\rho_Y+x_Y.
\tag{11.1}
\]
Together with (6.8), it gives the capacity
\[
t_{\Omega\setminus Y}
\leq
\min\left\{
6,\
c_Y+\rho_Y+(6-V_Y)_+
\right\}.
\tag{11.2}
\]

### Theorem 11.1: finite joint-run capacity gate

\[
\boxed{
\#\left\{
Y:
c_Y+\rho_Y+(6-V_Y)_+=0
\right\}
\leq11.
}
\tag{11.3}
\]
Also,
\[
\boxed{
126
\leq
\sum_Y
\left(
\min\{6,c_Y+\rho_Y+(6-V_Y)_+\}-1
\right)_+.
}
\tag{11.4}
\]

Equations (11.3)--(11.4), together with
\[
V_Y=W_Y+b_Y+u_{4,Y},
\qquad
\sum_{\ell\geq5}(\ell-3)\leq7,
\tag{11.5}
\]
are the strongest finite scalar gate produced by this attack.

#### Proof

If the right side of (11.2) is zero, the color is forced missing; there
are at most eleven missing colors. For every color, its duplicate
contribution is bounded above by the right side of (11.2) minus one when
positive. Summing and using \(\Delta_7\geq126\) proves (11.4).
\(\square\)

### Central/outer restitution

Let \(z_C,z_O\) be the central-core and outer supports, and let
\[
o_{CO}=|\operatorname{supp}C\cap\operatorname{supp}O|.
\tag{11.6}
\]
Put
\[
\Delta_C=N_C-z_C,
\qquad
D_O=N_O-z_O.
\tag{11.7}
\]
Then
\[
\boxed{
\Delta_7=\Delta_C+D_O+o_{CO}.
}
\tag{11.8}
\]

Decompose the postcut central color word into lazy folds and separated
returns:
\[
\Delta_C=A_C+S_C.
\tag{11.9}
\]
This decomposition is made directly on the postcut core word. At an
internal \(\eta=0\) seam it is not the uncorrected sum of the literal
quantities in (5.11)--(5.12); the exact correction is (5.23).
Therefore
\[
\boxed{
\Delta_7=A_C+S_C+D_O+o_{CO}.
}
\tag{11.10}
\]
At least one of the four nonnegative terms is at least \(32\). Splitting
\(S_C\) gives an exact five-gate version. Namely, when the internal seam
creates left and right core words,
\[
\Delta_C
=A_C+(S_L+S_R)+o_{LR},
\]
where \(S_L,S_R\) are the separated-return counts within the two words and
\(o_{LR}\) is their support overlap. For a single core word put
\(o_{LR}=0\) and \(S_L+S_R=S_C\). Hence
\[
\Delta_7
=A_C+(S_L+S_R)+o_{LR}+D_O+o_{CO},
\]
so one of these five nonnegative terms is at least \(26\).

The amount of central duplicate pressure satisfies
\[
\boxed{
\Delta_C
\geq
\max\{0,132+M_7-E-b_H\}.
}
\tag{11.11}
\]
If \(a\) is the number of rank-seven colors first introduced outside the
central core, then
\[
\boxed{
a=E+b_H-132-M_7+\Delta_C.
}
\tag{11.12}
\]
The outer repetition load is
\[
\boxed{
N_O-a=\Delta_7-\Delta_C.
}
\tag{11.13}
\]
Combining this identity with the endpoint-charged upper bound (5.27)
gives the conditional lower bound
\[
\boxed{
N_O-a=D_O+o_{CO}
\geq
\max\{0,\ M_7+b_H-c-\varepsilon_*\}.
}
\tag{11.14}
\]

#### Proof

For two multisets, total duplicate excess is the sum of the two internal
duplicate excesses plus the number of colors present on both sides, giving
(11.8). Equation (11.9) is Theorem 4.1 on the central core.

Adding \(N_O\) outer occurrences can increase duplicate excess by at most
\(N_O\), so
\[
\Delta_C\geq\Delta_7-N_O.
\]
Substitute (2.12) and (6.3) to obtain (11.11).

The global support is
\[
330-M_7=(N_C-\Delta_C)+a.
\]
Use \(N_C=m-3-b_H=462-E-b_H\) to obtain (11.12).
Equation (11.13) follows from \(N_O=E+b_H-c\).
Finally, substitute
\(\Delta_7=132-c+M_7\) and
\(\Delta_C\leq132-b_H+\varepsilon_*\) into (11.13) to get (11.14).
\(\square\)

There is no uniform positive lower bound on the duplicate pressure introduced
outside the central core,
\[
N_O-a=D_O+o_{CO}.
\]
This quantity includes central/outer support overlap and is not merely the
internal duplicate excess of the external-headed multiset. At the scalar
level it can range from essentially zero to all \(126\) units.

## 12. A short literal rank-eight lift

Let \(c_0\) be the number of isolated six-set components. A path with
\(v\geq2\) vertices has \(v-2\) adjacent pairs of forest edges, while an
isolated vertex has none. Thus the exact total is
\[
462-2c+c_0,
\]
and in particular there are at least
\[
462-2c
\tag{12.1}
\]
such adjacent pairs.

At most \(\mathcal A_7\leq\Delta_7\) are lazy, meaning their two
rank-seven hull colors coincide. Thus the number of nonlazy adjacent pairs
is at least
\[
\boxed{
462-2c+c_0-\Delta_7
=330-c-M_7+c_0
\geq313.
}
\tag{12.2}
\]

### Theorem 12.1: width-five rank-eight colors

Every nonlazy adjacent pair in (12.2) gives a literal rank-eight interval
of physical width at most five. A fixed rank-eight color occurs this way
at most \(26\) times. Consequently there are at least
\[
\boxed{
\left\lceil\frac{313}{26}\right\rceil=13
}
\tag{12.3}
\]
distinct literal rank-eight colors of width at most five.

#### Proof

Two adjacent hulls are formed from three consecutive selected rank-six
witnesses. Their physical union is contiguous and has width at most five,
because rank-six endpoint offsets lie between zero and three.

The two rank-seven colors share the middle six-set. If they are distinct,
their union has rank eight.

Fix an eight-set \(R\). It has
\[
\binom{8}{6}=28
\]
six-subsets. An occurrence is centered at a degree-two vertex of the
subforest induced by those \(28\) vertices. A linear forest on \(28\)
vertices has at most \(26\) degree-two vertices. This proves the
multiplicity cap and (12.3).
\(\square\)

This is a short-witness theorem, not a contradiction: \(13\) is far below
\(\binom{11}{8}=165\).

## 13. Exact scalar barriers

Two opposite scalar ledgers show why the new inequalities do not yet close.
Neither is asserted to be a common-word or set-labelled construction.

### 13.1 Central-loaded duplicates

Take
\[
c=6,\qquad M_7=11,\qquad m=330,\qquad
E=135,\qquad b_H=2,\qquad d=0.
\]
Then
\[
N_C=325,\qquad N_O=131.
\]
Choose an internal seam with \(\eta>0\), so \(c_Y=W_Y\). Partition the
\(330\) colors and assign their scalar data as follows:
\[
\begin{array}{c|c|c|c|c|c|c|c}
\text{number}&\text{role}&V_Y&W_Y&b_Y&u_{4,Y}&\rho_Y&x_Y\\ \hline
126&\text{central double}&5&2&1&2&0&0\\
62&\text{central single}&5&1&1&3&0&0\\
11&\text{central single+external}&5&1&1&3&0&1\\
120&\text{external single}&5&0&0&5&0&1\\
7&\text{missing}&4&0&0&4&0&0\\
4&\text{missing}&3&0&0&3&0&0
\end{array}
\tag{13.1}
\]
Thus
\[
z_C=126+62+11=199,\qquad
\sum_YW_Y=325=N_C,
\]
\[
z_7=199+131-11=319,
\qquad
\Delta_7=126+11=137.
\]
Moreover,
\[
\sum_YV_Y=319\cdot5+7\cdot4+4\cdot3=1635=5q.
\]
For every row, \(V_Y=W_Y+b_Y+u_{4,Y}\). Every external occurrence has
\(V_Y=5\), so \(x_Y=1=(6-V_Y)_+\). Thus this is a complete integer model
of the support, duplicate, joint-run, aggregate facet-star, and
central/external capacity equations.

### 13.2 Outer-loaded duplicates

Take
\[
E=132,\qquad m=333,\qquad b_H=2,\qquad
c=6,\qquad d=2,\qquad M_7=0.
\]
Then
\[
N_C=328,\qquad N_O=128,\qquad R_{\rm ext}=126.
\]
Again choose an internal seam with \(\eta>0\). Use the following partition:
\[
\begin{array}{c|c|c|c|c|c|c|c}
\text{number}&\text{role}&V_Y&W_Y&b_Y&u_{4,Y}&\rho_Y&x_Y\\ \hline
126&\text{central single+external}&5&1&1&3&0&1\\
200&\text{central single}&5&1&1&3&0&0\\
2&\text{central single}&4&1&1&2&0&0\\
2&\text{interface single}&6&0&0&6&1&0
\end{array}
\tag{13.2}
\]
Then
\[
z_7=330,\qquad
\sum_YW_Y=328=N_C,\qquad
\Delta_7=126.
\]
The facet-star sum is exactly
\[
\sum_YV_Y=326\cdot5+2\cdot4+2\cdot6=1650=5q.
\]
The \(126\) external-headed occurrences have \(V_Y=5\) and saturate
\(x_Y\leq6-V_Y\); the two central-inactive colors have \(V_Y=6\) and are
supported only by the two interfaces.

These ledgers prove that:

* support and duplicate counts do not force central repetition;
* they do not force external novelty;
* the two interfaces can absorb the only high-star inactive colors;
* the aggregate facet capacity (6.11) cannot contradict.

The ledgers certify only the aggregate support/multiplicity and facet-star
relaxation. They do not realize the simple head-label matrix, any physical
Hall system, the endpoint-width constraints, or a common word, and hence
do not prove that a physical survivor exists.

## 14. Strongest exact physical-lift theorem

The results can be compressed as follows.

### Theorem M3-K11

Every hypothetical length-\(465\) zero-margin survivor induces an integral
system satisfying all of the following.

1. A physical rank-seven hull family of \(462-c\) intervals, each of width
   at most four, with support at least \(319\), missing count at most \(11\),
   and duplicate excess \(132-c+M_7\).

2. For every four-set \(Y\), central joint-zero data
   \[
   V_Y=\sum(\ell-3)_+\leq7,\qquad
   W_Y=\sum(\ell-4)_+,
   \]
   with
   \[
   V_Y=W_Y+b_Y+u_{4,Y},
   \qquad W_Y+b_Y\leq7.
   \]
   Their postcut support satisfies
   \[
   |\{Y:c_Y=0\}|\leq E+1,
   \qquad
   \Delta_C\leq131,
   \]
   with the exact seam refinements (5.26)--(5.27).

3. A central/outer multiplicity split
   \[
   t_{\Omega\setminus Y}
   =c_Y+\rho_Y+x_Y,
   \]
   where
   \[
   x_Y\leq(6-V_Y)_+,\qquad
   \sum_Y\rho_Y=d\leq2.
   \]

4. The finite support and duplicate gates (11.3)--(11.4), including the
   high-star restriction
   \[
   \#\{Y:c_Y=0,V_Y\geq6\}\leq13.
   \]

5. A simple global head-label matrix with row sums \(t_Q\) and column sums
   \(42-\pi_x\), whose external submatrix has column sums
   \[
   43-R_x^{(3)}-\mathbf1_{\{x\in H\}}-\iota_x.
   \]

6. The nested head-label Hall system (8.12), the pair Hall system
   (8.17)--(8.19), and the complement-star Hall system (9.4)--(9.6).

7. External complement flags
   \[
   Y\subset\widehat D,\widehat D'\subset\widehat C
   \]
   with two distinct labels, factor-three matching-label exposure, and
   factor-four pair exposure.

8. At least \(13\) distinct literal rank-eight colors of physical width at
   most five.

No one of these projections is contradictory. A proof of nonexistence must
force a violation of one of the set-valued Hall cuts, or prove that the
joint-zero systems cannot be simultaneously realized by the same
rank-at-most-three entries in the fixed endpoint order.

## 15. Audit and exact remaining gate

The decisive constants have independent checks.

1. **Seven-facet audit.**  
   \(V_Y\leq7\) counts the seven five-set supersets of \(Y\).
   \(x_Y\leq6-V_Y\) is the forest edge cap on the remaining
   \(7-V_Y\) external facets.

2. **Edge-count audit.**  
   \[
   (q-b_H)+d+(E+b_H-c-d)=462-c.
   \]
   Thus no interface or external-headed edge is omitted or counted twice.

3. **Duplicate audit.**  
   \[
   \Delta_7=(462-c)-(330-M_7)=132-c+M_7.
   \]
   Both the lazy-return decomposition and the central/outer decomposition
   sum to this same number.

4. **Exposure audit.**  
   The matching label reaches three directed offsets. The predecessor label
   adds exactly the opposite one-cell offset, so the union of possible
   anchor offsets has size four, not six and not five.

5. **Interface audit.**  
   Complement-star Hall loses \(I_Z\leq d\); omitting this term would
   incorrectly force an interface-supported color onto an external anchor.

6. **Hall scope audit.**  
   Equation (8.8) is necessary and sufficient only for the simple
   coordinate-label matrix. The physical lift additionally requires the
   fixed predecessor equation (8.20), literal anchor containment, and the
   offset order.

7. **Local sharpness audit.**  
   The explicit ten-entry construction (5.20) realizes six consecutive
   equal rank-seven hull colors using rank-three entries while keeping all
   nine pair colors and all eight triple colors distinct. Therefore no
   universal replacement of the multiplicity-six cap by five follows even
   from the full local ordinary rank-four/rank-five/rank-six geometry.

8. **Lazy-index audit.**  
   Since \(Q_i=U_i\cup U_{i+1}\), two equal consecutive hulls have common
   facet \(U_{i+1}\). Thus the restitution coordinate is exactly
   \[
   Q\setminus U_{i+1}=\beta_i=\alpha_{i+2}.
   \]
   Using \(U_i\) here would be an off-by-one error.

9. **Seam-support audit.**  
   Literal five-window multiplicities and postcut central multiplicities
   differ only at the internal \(\eta=0\) seam, by exactly (5.21)--(5.23).
   Endpoint charging is applied before that deletion, and hence loses the
   single explicit \(\varepsilon_*\) in (5.26)--(5.27).

10. **Scalar-ledger audit.**  
    In (13.1) and (13.2), respectively,
    \[
    \sum_YW_Y=325,328,
    \qquad
    \sum_YV_Y=1635,1650,
    \]
    exactly matching \(N_C\) and \(5q\). The external and interface margins
    are also exactly \(R_{\rm ext}\) and \(d\). These checks certify only
    the stated aggregate relaxation.

The low-entry/seam derivation, the external Hall derivation, and the global
duplicate/width derivation were independently re-audited after the
corrections above; all three passed.

The remaining unproved statement is precise:

> There is no common rank-at-most-three central word and no ordered external
> anchor family simultaneously realizing (5.2)--(5.9), (6.8)--(6.10),
> the simple head-label matrix, the depth-two complement flags, the nested
> Hall cuts, and the at most two inward interfaces.

That incompatibility is not proved here. Accordingly this report does not
improve the certified interval for \(\nu(11)\).
