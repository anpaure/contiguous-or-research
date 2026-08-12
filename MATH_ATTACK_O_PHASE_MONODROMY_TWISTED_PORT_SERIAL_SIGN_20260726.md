# Lane O: phase monodromy and the fixed-exterior twist obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Corrected outcome

The phase-layer closure problem has two exact answers.

First, a genuinely two-cut-balanced first relative matching closes
positively. If the first matching is \(\pi\), the adjacent inverse

\[
 \sigma_0=\pi,\qquad \sigma_1=\pi^{-1},\qquad
 \sigma_t=1\quad(t\ge2)                               \tag{0.1}
\]

has product one. Its labelled two-cut \(Y\)-palette equation is precisely
the remaining ownership condition.

Second, geometric mirror pairing is not the same construction. Mirror plus
phase reversal sends

\[
             \sigma_t\longmapsto
             \omega\sigma_{r-1-t}^{-1}\omega,          \tag{0.2}
\]

where \(\omega\) is reverse-complement on Dyck roots. For \(r=2h\), a
mirror-paired schedule has monodromy

\[
                         \omega A^{-1}\omega A,
 \qquad A=\sigma_{h-1}\cdots\sigma_0,                 \tag{0.3}
\]

and closes if and only if \(A\omega=\omega A\). Mirror also sends a
palette discrepancy \(d\) to \(R_*d\), not to \(-d\).

The proposed escape was to allow an aligned local factor to have a port
twist

\[
                         P\longmapsto J\setminus\tau(P)               \tag{0.4}
\]

and cancel \(\tau\) in a later slab. Abstractly, such open path covers
and their permutation composition make sense. They are **not** legal
fixed-exterior Section-17 substitutions when \(\tau\ne1\).

The decisive reason is geodesicity. Every minimum wreath row is an
\(m\)-step Johnson geodesic between complementary \(m\)-sets, so every
contiguous subpath is geodesic. An aligned \(r\)-step slab with fixed
exterior \(O\), starting at \(O\cup P\) and ending at
\(O\cup(J\setminus\tau(P))\), has Johnson distance

\[
                         |P\cap\tau(P)|.               \tag{0.5}
\]

This equals the slab length \(r\) only when \(\tau(P)=P\). Hence

\[
 \boxed{\text{every fixed-exterior twisted minimum slab has }
        \tau=1\text{ pointwise}.}                     \tag{0.6}
\]

A later inverse twist cannot repair an earlier nongeodesic segment.
Therefore two nonidentity boundaries cannot add a quota improvement while
their twists cancel inside the ordinary fixed-exterior interface: those
boundaries do not exist as literal minimum-wreath subslabs.

There is one exact escape. If the exterior changes from \(O_L\) to
\(O_R\), with

\[
                         e=|O_L\setminus O_R|,
\]

then

\[
 d_J\bigl(O_L\cup P, O_R\cup(J\setminus Q)\bigr)
                         =e+|P\cap Q|.                 \tag{0.7}
\]

An \(r\)-step geodesic with \(Q=\tau(P)\) is possible only if

\[
                         e=|P\setminus\tau(P)|.         \tag{0.8}
\]

Thus exterior motion must pay exactly for the local twist. Such an object
is a larger boundary-moving trade whose full exterior \(X/Y\) ledgers and
carrier profile must be rebuilt. It is not a twisted substitution into a
fixed Section-17 hole.

For completeness, endpoint inversion by itself carries no profile minus
sign in an abstract or exterior-moving model. A physical mirror exchanges
first insertion with reflected last deletion. This conditional sign
calculus is proved below, but it gives no current literal fixed-exterior
construction and no constant-one theorem.

## 1. Fixed-layer relative matchings

Let \(J=[2r]\), let \(D=D_{2r}^0\) be the Dyck roots, and let

\[
                         i_t:D\longrightarrow L_t=D_{2r}^t,
                         \qquad0\le t\le r,             \tag{1.1}
\]

be the canonical Chung--Feller phase bijections. The endpoint theorem is

\[
                         i_r(P)=J\setminus i_0(P).       \tag{1.2}
\]

For phase permutations \(p_t\in\operatorname {Sym}(D)\), put

\[
                         X_t(P)=i_t(p_tP),
 \qquad                 \sigma_t=p_{t+1}p_t^{-1}.       \tag{1.3}
\]

The exact fixed-layer equations are Johnson legality,

\[
                         i_t(u)\sim_Ji_{t+1}(\sigma_tu),               \tag{1.4}
\]

the complete labelled \(Y\)-palette,

\[
 \sum_{t=0}^{r-1}\sum_{u\in D}
 e_{i_t(u)\cup i_{t+1}(\sigma_tu)}
                         =\mathbf1_{\binom J{r+1}},     \tag{1.5}
\]

and zero monodromy,

\[
                         \sigma_{r-1}\cdots\sigma_0=1.               \tag{1.6}
\]

Equation (1.5), not coordinate marginal balance, is the exact upper-shore
ownership condition.

### Theorem 1.1 (adjacent-inverse completion)

Let \(r\ge2\) and \(\pi\in\operatorname {Sym}(D)\). Suppose that for
every \(P\in D\),

\[
                         i_0(P)\sim_Ji_1(\pi P)\sim_Ji_2(P),           \tag{1.7}
\]

and that the two incident palettes balance label by label:

\[
\begin{aligned}
 \sum_{P\in D}\bigl(
 e_{i_0(P)\cup i_1(\pi P)}
 +e_{i_1(\pi P)\cup i_2(P)}\bigr)
 ={}&
 \sum_{P\in D}\bigl(
 e_{i_0(P)\cup i_1(P)}
 +e_{i_1(P)\cup i_2(P)}\bigr).                         \tag{1.8}
\end{aligned}
\]

Then

\[
                         p_0=1,quad p_1=\pi,quad
                         p_t=1\quad(2\le t\le r)       \tag{1.9}
\]

is an exact fixed-layer factor. Equivalently its relative matchings are
(0.1).

#### Proof

The permutation \(\pi\) preserves the phase-one \(X\)-ledger. Equation
(1.7) supplies all changed Johnson edges and (1.8) supplies exactly the
changed part of the \(Y\)-ledger. Every later cut is canonical. Finally
\(\pi^{-1}\pi=1\), so the endpoints close rowwise. \(\square\)

This theorem is positive and literal. It uses one ordinary zero-monodromy
phase packet, not two independently twisted local holes.

## 2. Mirror action and its central involution

Let \(R(j)=2r+1-j\), and let

\[
                         \omega(P)=R(J\setminus P).     \tag{2.1}
\]

Literal MSW path reversal gives

\[
                         R\,i_{r-t}(P)=i_t(\omega P)    \tag{2.2}
\]

for all \(P,t\). After reversing phases, applying \(R\), and reanchoring
the roots,

\[
                         (\mathfrak Mp)_t=\omega p_{r-t}\omega,        \tag{2.3}
\]

so

\[
 \boxed{(\mathfrak M\sigma)_t
                         =\omega\sigma_{r-1-t}^{-1}\omega.}           \tag{2.4}
\]

If

\[
 U_t(\sigma)=\sum_{P\in D}
 e_{i_t(P)\cup i_{t+1}(\sigma P)},                     \tag{2.5}
\]

then

\[
 U_{r-1-t}((\mathfrak M\sigma)_{r-1-t})
                         =R_*U_t(\sigma_t).             \tag{2.6}
\]

Thus a cut discrepancy \(d_t=U_t(\sigma_t)-U_t(1)\) is paired with
\(R_*d_t\). Mirror-palette cancellation needs the additional identity

\[
                         d_t+R_*d_t=0.                  \tag{2.7}
\]

### Theorem 2.1 (mirror-paired monodromy)

Assume

\[
                         \sigma_t
             =\omega\sigma_{r-1-t}^{-1}\omega.         \tag{2.8}
\]

If \(r=2h\) and \(A=\sigma_{h-1}\cdots\sigma_0\), then

\[
 \boxed{\operatorname {Mon}(\sigma)=\omega A^{-1}\omega A.}          \tag{2.9}
\]

It closes if and only if

\[
                         A\omega=\omega A.             \tag{2.10}
\]

If \(r=2h+1\), the central cut obeys

\[
                         \sigma_h=\omega\sigma_h^{-1}\omega.
\]

Putting \(\eta=\omega\sigma_h\), one has \(\eta^2=1\) and

\[
 \boxed{\operatorname {Mon}(\sigma)=\omega A^{-1}\eta A.}            \tag{2.11}
\]

It closes if and only if

\[
                         \eta=A\omega A^{-1}.          \tag{2.12}
\]

#### Proof

For \(r=2h\), the descending product of the upper-half mirror matchings is

\[
 (\omega\sigma_0^{-1}\omega)\cdots
 (\omega\sigma_{h-1}^{-1}\omega)=\omega A^{-1}\omega.
\]

Multiplying by \(A\) proves (2.9), and setting it equal to one gives
(2.10). The odd case leaves the central factor \(\sigma_h\), giving
(2.11); its self-mirror equation is \(\eta^2=1\), while closure is
(2.12). \(\square\)

This obstruction belongs to geometric mirror pairing. It does not affect
the adjacent-inverse completion of Theorem 1.1.

Statewise reverse-complement without phase reversal is unsafe: for adjacent
states \(X,X'\),

\[
 \omega X\cup\omega X'=R\bigl(J\setminus(X\cap X')\bigr),             \tag{2.13}
\]

so it requires a separate exact intersection ledger.

## 3. Abstract twisted path covers

Let \(D\subseteq\binom Jr\) satisfy
\(D\cap\overline D=\varnothing\), with

\[
                         \overline D=\{J\setminus P:P\in D\}.
\]

### Definition 3.1

For \(\tau\in\operatorname {Sym}(D)\), an abstract
\(\tau\)-twisted path cover is a vertex partition of the local
middle-levels inclusion graph into paths

\[
 P=X_0\subset Y_0\supset X_1\subset\cdots\subset
 Y_{r-1}\supset X_r=J\setminus\tau(P),qquad P\in D. \tag{3.1}
\]

Each path has \(r\) Johnson steps. In fixed-layer coordinates its relative
matching product is

\[
                         \sigma_{r-1}\cdots\sigma_0=\tau.              \tag{3.2}
\]

Both local shores may be owned exactly even when \(\tau\ne1\). Such a
row is not an odd cycle: its closing Kneser edge exists if and only if

\[
 P\cap(J\setminus\tau(P))=\varnothing,
\]

equivalently \(\tau(P)=P\).

There is an exact quota conservation law even in this abstract category.
Write one transition as

\[
                         X_{t+1}=X_t-a_{t+1}+b_{t+1}.
\]

For every coordinate \(x\in J\),

\[
 \boxed{
 \sum_{P,t}\mathbf1_{\{b_{t+1}(P)=x\}}
       =\#\{P\in D:x\notin P\},}                       \tag{3.2a}
\]

and

\[
 \boxed{
 \sum_{P,t}\mathbf1_{\{a_{t+1}(P)=x\}}
       =\#\{P\in D:x\in P\}.}                         \tag{3.2b}
\]

Indeed, \(b_{t+1}=Y_t\setminus X_t\). The \(Y_t\)'s enumerate
\(\binom J{r+1}\), while the nonterminal \(X_t\)'s enumerate every
\(r\)-set except \(\overline D\). Therefore the insertion count is

\[
 \binom{2r-1}{r}
 -\left(\binom{2r-1}{r-1}
       -\#\{Q\in\overline D:x\in Q\}\right),
\]

which is the right side of (3.2a). The deletion identity follows in the
same way because the noninitial \(X\)-states omit exactly \(D\).

Hence a changed first-insertion histogram is compensated among later
insertion columns of the **same** exact local shore ledger. It is not
assigned a negative sign by an inverse endpoint permutation.

If two abstract open covers have twists \(\tau,\rho\) and an interface
identifies their labels by \(\alpha\), the formal transported product is

\[
                         \alpha^{-1}\rho\alpha\tau.     \tag{3.3}
\]

Thus the formal inverse condition is

\[
                         \rho=\alpha\tau^{-1}\alpha^{-1}.              \tag{3.4}
\]

Equations (3.3)--(3.4) are correct permutation algebra. They do not prove
that the two open covers occur as contiguous subpaths of one literal
minimum wreath.

## 4. The decisive fixed-exterior geodesic obstruction

For equal-size sets in a Johnson graph,

\[
                         d_J(A,B)=|A\setminus B|
                                  =m-|A\cap B|.         \tag{4.1}
\]

### Lemma 4.1 (every subpath of a minimum wreath is geodesic)

Let

\[
                         A_0,A_1,\ldots,A_m            \tag{4.2}
\]

be the Johnson trace of a minimum wreath row, so every consecutive pair is
adjacent and \(A_m=[2m]\setminus A_0\). Then every subpath
\(A_a,\ldots,A_b\) has

\[
                         d_J(A_a,A_b)=b-a.              \tag{4.3}
\]

#### Proof

The endpoints in (4.2) are complementary, so their Johnson distance is
\(m\), equal to the number of steps. If
\(d_J(A_a,A_b)<b-a\), replace that subpath by a shortest path. Together
with the old prefix and suffix this gives a walk from \(A_0\) to \(A_m\)
of length less than \(m\), contradicting their distance. \(\square\)

### Theorem 4.2 (fixed-exterior twist rigidity)

Let \(J\) be a local coordinate set of size \(2r\), let \(O\) be a fixed
exterior set of size \(m-r\), and suppose an \(r\)-step contiguous subpath
of a minimum wreath has endpoints

\[
                         A=O\cup P,qquad
                         B=O\cup(J\setminus\tau(P)),    \tag{4.4}
\]

where \(P,\tau(P)\in\binom Jr\). Then

\[
                         \tau(P)=P.                    \tag{4.5}
\]

Consequently a family of such slabs has pointwise identity twist.

#### Proof

The intersection in (4.4) has size

\[
\begin{aligned}
 |A\cap B|
   &=|O|+|P\cap(J\setminus\tau(P))|\\
   &=(m-r)+(r-|P\cap\tau(P)|)\\
   &=m-|P\cap\tau(P)|.
\end{aligned}                                           \tag{4.6}
\]

Therefore

\[
                         d_J(A,B)=|P\cap\tau(P)|.       \tag{4.7}
\]

Lemma 4.1 says that this distance equals the subpath length \(r\). Hence
\(|P\cap\tau(P)|=r\), and two \(r\)-sets with intersection \(r\) are
equal. \(\square\)

### Corollary 4.3 (serial inverse cannot repair the detour)

No sequence of nonidentity fixed-exterior twisted slabs can occur in one
minimum wreath, even if its formal product (3.3) is one.

#### Proof

Theorem 4.2 applies separately to the first purported nonidentity slab.
Equivalently, a globally geodesic path cannot contain a nongeodesic
subpath and later cancel its excess length. \(\square\)

This is stronger than a monodromy obstruction. It rules out the local
objects before their endpoint permutations are multiplied.

### Corollary 4.4 (metric defects add)

Let a Johnson walk from an \(m\)-set to its complement contain pairwise
disjoint fixed-exterior twisted slabs of lengths \(r_i\), with local ports
\(P_i\) and twists \(\tau_i\). Its length excess over the complement
distance \(m\) is at least

\[
 \boxed{\sum_i\bigl(r_i-|P_i\cap\tau_i(P_i)|\bigr)
       =\sum_i|P_i\setminus\tau_i(P_i)|.}              \tag{4.8}
\]

In particular, composing \(\tau\) with \(\tau^{-1}\) may cancel the
permutation but cannot cancel either nonnegative metric defect.

#### Proof

Replace each disjoint slab by a shortest path between its own endpoints.
The resulting walk has the same global endpoints and is shorter by the
sum in (4.8). Since every walk between complementary \(m\)-sets has length
at least \(m\), the original excess is at least that sum. \(\square\)

## 5. Exact boundary-changing escape

The fixed-exterior hypothesis is the precise issue, not the notation
\(\tau\).

Let \(O_L,O_R\) be exterior \((m-r)\)-sets disjoint from \(J\), and put

\[
                         e=|O_L\setminus O_R|
                          =(m-r)-|O_L\cap O_R|.          \tag{5.1}
\]

### Theorem 5.1 (exterior/local distance decomposition)

For \(P,Q\in\binom Jr\),

\[
 \boxed{
 d_J\bigl(O_L\cup P, O_R\cup(J\setminus Q)\bigr)
                         =e+|P\cap Q|.}                \tag{5.2}
\]

Hence an \(r\)-step geodesic with \(Q=\tau(P)\) exists only if

\[
 \boxed{e=r-|P\cap\tau(P)|=|P\setminus\tau(P)|.}       \tag{5.3}
\]

#### Proof

The endpoint intersection is

\[
                         (O_L\cap O_R)
           \mathbin{\dot\cup}(P\cap(J\setminus Q)),
\]

of size

\[
                         (m-r-e)+(r-|P\cap Q|)
                         =m-e-|P\cap Q|.
\]

Substitution in (4.1) proves (5.2). Setting the distance equal to \(r\)
gives (5.3). \(\square\)

### Corollary 5.2 (exact exchange menu)

Under the equality condition (5.3), every \(r\)-step path between the
displayed endpoints is geodesic. It deletes each member of

\[
 \boxed{(O_L\setminus O_R)\mathbin{\dot\cup}(P\cap Q)}                \tag{5.4}
\]

once, inserts each member of

\[
 \boxed{(O_R\setminus O_L)\mathbin{\dot\cup}
        \bigl(J\setminus(P\cup Q)\bigr)}               \tag{5.5}
\]

once, and exchanges no other coordinate.

#### Proof

The two displayed sets are exactly the left endpoint minus the right and
the right endpoint minus the left. A shortest Johnson path exchanges every
coordinate in these two differences exactly once. Their common size is

\[
                         e+|P\cap Q|=r
\]

by (5.2)--(5.3). \(\square\)

Thus exterior coupling does not merely pay a scalar distance toll: it
changes the literal deletion and insertion menus. Any first-edge quota
claim must specify where the exterior coordinates occur in these two
orders.

Thus every unit of local endpoint mismatch needs one unit of exterior
Johnson motion. The exterior boundary is then part of the trade. Its
states, union colours, collars, and carrier tags cannot be inherited from
the fixed-context substitution theorem.

Although the abstract local factor still has the formal palette

\[
                         \biguplus_{P,t}Y_t(P)=\binom J{r+1},          \tag{5.6}
\]

this does not settle the ambient \(Y\)-ledger after exterior motion. With
a common fixed exterior, one simply pushes every local colour through the
same injection. When \(O_L\ne O_R\), the exterior present at an
intermediate colour depends on the actual coupled route. Two equal local
colours can therefore acquire different ambient carriers, or two different
local occurrences can collide. Exactness must be checked on the literal
ambient colours, occurrence by occurrence.

Crossing the cyclic closing edge is another different architecture; it is
not an \(r\)-step Johnson subslab and is not covered by Definition 3.1.

## 6. Audit of the abstract serial-twist proposal

This section also audits
`MATH_THEOREM_TWISTED_PORT_MONODROMY_COMPOSITION_20260726.md`.

The following parts of the serial proposal are valid.

1. A spanning open path cover with endpoint sets \(D,\overline D\)
   determines an endpoint permutation.
2. If every component has exactly \(2r\) inclusion edges, it has the
   abstract form (3.1).
3. The permutation product (3.3) is the correct formal label product.
4. Each abstract cover may own both local shores exactly.
5. Physical mirror plus path reversal sends

   \[
                         \tau\longmapsto
                         \omega\tau^{-1}\omega.        \tag{6.1}
   \]

The invalid implication in the fixed-exterior minimum-wreath application
is

\[
\begin{aligned}
 &\text{exact local shores + equal component lengths + final label product }1\\
 &\hspace{35mm}\Longrightarrow
   \text{literal aligned minimum-wreath substitution}.               \tag{6.2}
\end{aligned}
\]

It omits Lemma 4.1. In a real serial path, the boundary state of the later
slab includes the exterior transported by the earlier tail permutation.
Matching only the local port label does not certify that this exterior is
the fixed one required by the later context. If all exteriors really are
fixed, Theorem 4.2 makes every twist trivial.

Accordingly, the inverse-packet and finite-order-repetition principles are
only statements about abstract open covers or a future boundary-moving
global construction. They are vacuous for nonidentity fixed-exterior
Section-17 holes.

More explicitly:

* Definition 1.1 and the endpoint-permutation bookkeeping are **valid as
  abstract open path-cover statements**.
* The claim that one nonidentity twisted slab can be reassembled into a
  fixed-exterior minimum ambient wreath merely by permuting old tails is
  **unsupported and false in that architecture** by Theorem 4.2.
* The serial product, inverse-packet, finite-order-repetition, and
  same-phase-hexagon statements are **valid formal open-cover algebra**,
  but their promotion to literal minimum-wreath substitutions is
  **refuted** unless exterior motion satisfying (5.3) is supplied.
* The conditional carrier-sign discussion remains correct for an actual
  boundary-moving construction, subject to the occurrencewise and
  cross-window qualifications in Section 7.

## 7. Conditional carrier-sign calculus

Although it supplies no present construction, it is useful to record what
endpoint inversion would imply in a valid exterior-moving or abstract
model.

Compare old and new two-slab systems. Retain every owner, offset, exterior
carrier, and local embedding. For a physical occurrence write

\[
 d=e_{O^+\cup\iota^+(S^+)}-e_{O^-\cup\iota^-(S^-)}.    \tag{7.1}
\]

Call two slabs \(q\)-influence-separated when no serviced \(q\)-window
meets changed states in both.

### Proposition 7.1 (no monodromy sign)

In any genuinely realizable, \(q\)-influence-separated two-slab system,
the signed physical load vector is the sum of the occurrence atoms from
the two slabs. In the port-local case it is

\[
 \boxed{D_q^{\rm total}=D_{1,q}+D_{2,q}.}              \tag{7.2}
\]

If the old first slab is untwisted, the new first slab has twist \(\tau\),
and the interface is \(\alpha\), the second-slab row contribution for an
initial owner \(P\) is

\[
                         n_2(\alpha\tau P)-o_2(\alpha P).              \tag{7.3}
\]

Summing (7.3) over \(P\) gives \(D_{2,q}\), because \(\alpha\tau\) and
\(\alpha\) are bijections. No inverse endpoint permutation introduces a
minus sign.

If a carrier remembers both the pre-twist owner and the local port, retain
(7.1) occurrencewise; (7.2) may not collapse, but there is still no
algebraic sign rule. If a window crosses both slabs, it is one joint atom
and marginal additivity is invalid.

#### Proof

Influence separation partitions the changed occurrences. Signed load
vectors use the same new-minus-old convention in both slabs, and owner
permutations only reindex the sums. \(\square\)

### Proposition 7.2 (mirror exchanges boundary columns)

For a trade \(F\to G\), let \(d^+\) be the signed first-insertion
histogram and \(d^-\) the signed last-deletion histogram. Under physical
mirror plus path reversal,

\[
 \boxed{d^+_{\rm mir}=R_*d^-,\qquad
        d^-_{\rm mir}=R_*d^+.}                        \tag{7.4}
\]

Indeed, if the last original step is

\[
                         X_r=X_{r-1}-a_r+b_r,
\]

then the first mirrored step is

\[
                         R(X_{r-1})=R(X_r)-R(b_r)+R(a_r).              \tag{7.5}
\]

Thus a mirror inverse has the same new-minus-old sign. With physical
carrier maps \(\Phi_1,\Phi_2\), first-edge cancellation requires the
extra targetwise identity

\[
                         (\Phi_2)_*R_*d^-
                         =-(\Phi_1)_*d^+.              \tag{7.6}
\]

It is not a consequence of inverse monodromy.

### Example 7.3 (identity-twist sign independence)

At \(r=2\), the two exact port factors

\[
 F:(12,14,34),(13,23,24),qquad
 G:(12,23,34),(13,14,24)                              \tag{7.7}
\]

have first-insertion discrepancy

\[
                         d^+=e_3-e_2.                  \tag{7.8}
\]

Their last-deletion discrepancy is \(d^-=e_2-e_3\), and for
\(R=(1\ 4)(2\ 3)\),

\[
                         R_*d^-=d^+.                   \tag{7.9}
\]

Two influence-separated aligned mirror copies therefore give
\(2(e_3-e_2)\), not zero. Both twists are \(1=1^{-1}\).

This proves that endpoint inversion has no universal profile sign. It does
**not** evade Theorem 4.2, because its twist is already identity.

## 8. Alternating hexagons: valid abstract routers, invalid fixed holes

Suppose one synchronized open path cover contains at a common phase the
three selected incidence edges

\[
\begin{array}{c|c}
 K\cup\{a\}&K\cup\{a,b\}\\
 K\cup\{b\}&K\cup\{b,c\}\\
 K\cup\{c\}&K\cup\{c,a\},
\end{array}                                             \tag{8.1}
\]

where \(|K|=r-1\). Toggling to the other half of the literal hexagon

\[
 Ka-Kab-Kb-Kbc-Kc-Kca-Ka                              \tag{8.2}
\]

preserves both degree ledgers and cyclically permutes equal-length
suffixes. It therefore creates an abstract three-cycle twist.

At the entrance, its row-resolved insertion discrepancy is, up to
orientation,

\[
\begin{aligned}
 d_{C_6}={}&e_{(P_a,c)}+e_{(P_b,a)}+e_{(P_c,b)}\\
            &-e_{(P_a,b)}-e_{(P_b,c)}-e_{(P_c,a)}.      \tag{8.3}
\end{aligned}
\]

Its unlabelled coordinate projection is zero, but distinct owner carriers
can retain (8.3).

Two later clean routers can formally compile an involution. For example,
with left actions

\[
                         \lambda_1=(1\ 2\ 3),qquad
                         \lambda_2=(1\ 4\ 3),
\]

the total twist is

\[
                         \lambda_2\lambda_1=(1\ 2)(3\ 4).             \tag{8.4}
\]

Two abstract copies then have product one while any protected entrance
profile occurs twice with the same formal sign.

This router algebra is correct, but it is not a fixed-exterior literal
construction. Theorem 4.2 forbids each resulting nonidentity open cover as
a Section-17 subslab. A useful router must be incorporated into one larger
boundary-moving geodesic satisfying (5.3), with every exterior state,
colour, and carrier audited. No such growing construction is proved.

## 9. Nonlinear cap caveat

Even in a valid boundary-moving construction, the signed load vector is
linear but

\[
                         K_p(h)=\sum_T(h(T)-p)_+
\]

is not. Mirror-related atoms on disjoint carrier slices double their hinge
effect only when the old loads and capacities are correspondingly related.
Opposite signed vectors on disjoint targets do not literally cancel. Exact
cancellation for every background requires targetwise zero after all
carrier pushforwards.

## 10. Final audited boundary

The following statements are proved.

1. Labelled two-cut balance closes by the adjacent inverse (0.1).
2. Geometric mirror pairing has the central obstruction (2.10) or (2.12)
   and same-sign reflected palette discrepancies.
3. Abstract twisted open path covers and the formal permutation product
   (3.3) are well-defined.
4. Their total insertion/deletion quotas obey (3.2a)--(3.2b), so prefix
   changes are compensated internally rather than by endpoint inversion.
5. Every contiguous subpath of a minimum wreath is Johnson-geodesic.
6. Fixed exterior forces every \(r\)-step local twist to be pointwise
   identity.
7. Nontrivial local twist requires exactly the exterior motion (5.3).
8. Conditional on an actually realizable influence-separated
   boundary-moving construction, inverse monodromy supplies no profile
   minus sign; mirror acts by (7.4).
9. The rank-two rectangle is an exact identity-twist counterexample to any
   universal inverse-profile negation law.
10. Same-phase hexagons are valid abstract endpoint routers but cannot be
   packaged as nonidentity fixed-exterior minimum slabs.

The following are unproved.

1. A boundary-moving exact factor with nonidentity local endpoint transport
   satisfying (5.3) on every row.
2. A serial or joint construction with exact exterior \(X/Y\) ledgers and
   favourable carrier sign.
3. A growing positive-density router supply.
4. A background-independent PCap decrease.
5. Any constant-one conclusion.

The central question is therefore resolved negatively in the intended
architecture: inverse twists do not force quota negation; rather,
nonidentity fixed-exterior twists are themselves impossible. The only
surviving version is a larger exterior-coupled global geodesic trade.
