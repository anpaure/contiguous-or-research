# Complement/c-space gap duality and the exact PBBS lift boundary

Date: 2026-07-29

Status: exact cyclic duality theorem, exact odd/even lift theorem, and an
explicit even-component counterexample.  The result removes one duplicate
shadow-decoration bank from a complement-closed carrier.  It does not prove
a PBBS fusion, residence after fusion, or a common compiler/owner lift.

## 0. Verdict

Complement coherence does translate the upper insertion-prefix condition
into a lower deletion-window condition, including occurrence multiplicity.
The translation is not same-depth:

\[
 \boxed{\text{upper depth }q\quad\longleftrightarrow\quad
        \text{lower depth }q+1.}
\]

The physical span is also retained.  A long upper first-arrival prefix maps
to a long lower deletion window, not automatically to the nominal shallow
erosion row.  Thus one complete cyclic lower flag bank supplies the upper
bank, but residence, endpoint collars, owner Hall, and compiler pins do not
collapse.

The odd/even lift has a sharp parity boundary.  An odd odd-graph component
lifts to one internally complement-coherent Middle Levels cycle.  An even
component lifts to two cycles exchanged by complement.  Rotation-equivariant
unit voltage transports either lifted component to a run-transversal binary
`c`-carrier after gauge; complement coherence alone does not supply that
equivariance.  Finally, the inverse-two permutation used to make the NAND
law local is not a physical chronology and cannot transport run
transversality.

## 1. Cyclic insertion/deletion duality

Let \(\Omega\) have size \(2m+1\), put \(r=m+1\), and let

\[
 T_i\in\binom{\Omega}{r}\qquad(i\in\mathbb Z_W)
\]

be a simple cyclic Johnson chronology.  Write its seam as

\[
 T_{i+1}=T_i-\{e_i\}+\{a_i\},                       \tag{1.1}
\]

and put \(X_i=T_i\cap T_{i+1}\).  Assume \(W=2s+1\) and the exact
complement half-turn

\[
 \boxed{\overline{T_i}=X_{i+s}.}                    \tag{1.2}
\]

All indices below are cyclic modulo \(W\).

### Theorem 1.1 (seam and interval duality)

For every \(i\),

\[
 \boxed{e_i=a_{i+s},\qquad a_i=e_{i+s+1}.}          \tag{1.3}
\]

For every width \(w\ge1\), define

\[
 U_{i,w}=\bigcup_{h=0}^{w-1}T_{i+h},\qquad
 L_{j,w+1}=\bigcap_{h=0}^{w}T_{j+h}.                \tag{1.4}
\]

Then

\[
\boxed{
 \overline{U_{i,w}}=L_{i+s,w+1}
 =T_{i+s}\setminus
   \{e_{i+s},e_{i+s+1},\ldots,e_{i+s+w-1}\}.}      \tag{1.5}
\]

At the same time,

\[
 U_{i,w}=T_i\cup\{a_i,a_{i+1},\ldots,a_{i+w-2}\}, \tag{1.6}
\]

where an empty displayed list is ignored and repetitions are harmless.
The baseline deletion \(e_{i+s}\) in (1.5) forms
\(\overline{T_i}=X_{i+s}\); the remaining deletion prefix is termwise the
upper insertion prefix:

\[
 a_{i+h}=e_{i+s+h+1}\qquad(0\le h\le w-2).         \tag{1.7}
\]

#### Proof

The lower chronology satisfies

\[
 X_{j+1}=X_j-\{e_{j+1}\}+\{a_j\}.                 \tag{1.8}
\]

On the other hand, complementing (1.1) gives

\[
 \overline{T_{i+1}}
   =\overline{T_i}-\{a_i\}+\{e_i\}.               \tag{1.9}
\]

Equations (1.2), (1.8), and (1.9), together with simplicity of the two
incident lower vertices, identify the unique deleted and inserted elements
and prove (1.3).

De Morgan's law and (1.2) give

\[
\begin{aligned}
 \overline{U_{i,w}}
 &=\bigcap_{h=0}^{w-1}\overline{T_{i+h}}\\
 &=\bigcap_{h=0}^{w-1}(T_{i+s+h}\cap T_{i+s+h+1})\\
 &=\bigcap_{h=0}^{w}T_{i+s+h}.
\end{aligned}                                       \tag{1.10}
\]

An intersection of consecutive Johnson states consists of the initial
state minus every coordinate deleted somewhere in the interval; coordinates
inserted and later deleted but absent initially do not affect this set
identity.  This proves the last expression in (1.5).  Formula (1.6) is the
dual elementary union identity, and (1.7) is (1.3).  \(\square\)

### Corollary 1.2 (exact load equality)

Put

\[
 \mu_w^+(S)=|\{i:U_{i,w}=S\}|,qquad
 \mu_{w+1}^-(R)=|\{j:L_{j,w+1}=R\}|.
\]

Then, for every \(S\subseteq\Omega\),

\[
 \boxed{\mu_w^+(S)=\mu_{w+1}^-(\overline S).}       \tag{1.11}
\]

This is an occurrence bijection, not merely a support equivalence: the
corresponding start is \(i\mapsto i+s\).

For the backward erosion convention

\[
 P_j^{(q)}=\bigcap_{b=0}^{q}T_{j-b},                \tag{1.12}
\]

the exact terminal index is

\[
 \boxed{
 \overline{\bigcup_{h=0}^{q}T_{i+h}}
   =P_{i+s+q+1}^{(q+1)}.}                           \tag{1.13}
\]

In particular, replacing the terminal index by \(i+s\) is an indexing
error.  If residence through depth \(q+1\) makes the right side have its
nominal rank \(r-q-1\), then the upper union has rank \(r+q\).  Same-depth
halving is impossible already by rank.

## 2. Exact c-space gap algebra

Suppose now \(W=kN\), \(k=2m+1\), and the chronology has the binary form

\[
 T_i=\{x\in\mathbb Z_k:c_{i-xN}=1\}.                \tag{2.1}
\]

Complement coherence is the physical-order scalar law

\[
 1-c_p=c_{p+s}c_{p+s+1}.                            \tag{2.2}
\]

For \(p(i,x)=i-xN\), define the next-insertion clock

\[
 \delta_i(x)=\min\{h\ge0:c_{p(i,x)+h}=1\},          \tag{2.3}
\]

and the shifted pair-failure clock

\[
 \kappa_j(x)=\min\{h\ge0:
   c_{j-xN+h}c_{j-xN+h+1}=0\}.                      \tag{2.4}
\]

The minima may be taken in \(\{0,\ldots,W-1\}\); the rank equations make
both symbols occur in every coordinate trace.

### Theorem 2.1 (next insertion equals next lower deletion)

For every \(i,x\),

\[
 \boxed{\delta_i(x)=\kappa_{i+s}(x).}               \tag{2.5}
\]

Consequently a proper upper target \(S\) is an insertion-prefix union
starting at \(i\) if and only if, with \(R=\overline S\) and \(j=i+s\),

\[
 \boxed{
 \max_{x\notin R}\kappa_j(x)
 <\min_{y\in R}\kappa_j(y).}                       \tag{2.6}
\]

If the left maximum is \(\ell\), then the shortest upper witness has
states \(T_i,\ldots,T_{i+\ell}\), while its exact lower mate is

\[
 R=\bigcap_{h=0}^{\ell+1}T_{j+h}.                  \tag{2.7}
\]

#### Proof

Substitute \(p=p(i,x)+h\) in (2.2).  The event
\(c_{p(i,x)+h}=1\) is exactly the event that

\[
 c_{i+s-xN+h}c_{i+s-xN+h+1}=0.
\]

Taking the first such \(h\) proves (2.5).  The exact next-occurrence upper
oracle says that \(S\) is a prefix union precisely when every required
coordinate arrives strictly before every forbidden coordinate.  Replacing
each \(\delta\) by \(\kappa\) gives (2.6).  Through time \(\ell\), every
coordinate outside \(R\) has failed at least one adjacent lower pair, while
every coordinate of \(R\) remains present in all \(\ell+2\) lower states.
This is (2.7).  \(\square\)

### Corollary 2.2 (what is and is not halved)

Theorems 1.1 and 2.1 remove one complete **all-width cyclic shadow shore**.
Equivalently, a complete nominal lower flag tower implies the complete
upper tower after the depth shift: a lower target of rank \(r-q-1\) at
depth \(q+1\) complements to an upper target of rank \(r+q\).

They do not identify every arbitrary-width upper prefix with the lower row
having the same rank-depth label.  The physical shortest span \(\ell\) can
exceed the rank increase \(q\) because insertions may be recycled before all
required coordinates have first appeared.  Its dual is then the equally
long lower window (2.7).  The nominal row occurs exactly in the tight case
\(\ell=q\).

Thus complement duality halves support and multiplicity tests, and it
transports any explicitly protected witness interval.  It does not by
itself halve or prove:

1. positive-run residence or short-return exclusions;
2. safe linear cuts and their two endpoint collars;
3. a common middle-owner Hall assignment;
4. compiler pin containment or a common literal word.

In particular, a cyclic lower witness beginning at \(j\) and of width
\(w+1\) reconstructs the upper witness beginning at \(j-s\) and of width
\(w\).  Whether either witness crosses a chosen linear cut must still be
checked at its own shifted start and span.

### Remark 2.3 (exact quotient carry)

When \(W=kN\) is odd, write

\[
 n=(N-1)/2,\qquad s=mN+n.
\]

For a quotient start \(0\le j<N\), put

\[
 j'=(j+n)\bmod N,qquad
 \epsilon_j=\left\lfloor\frac{j+n}{N}\right\rfloor.
\]

If \(T_{i+N}=\rho^vT_i\), (1.5) reads on chosen quotient
representatives as

\[
 \boxed{
 \overline{U_{j,w}}
   =\rho^{v(m+\epsilon_j)}L_{j',w+1}.}              \tag{2.8}
\]

This is the forced sheet carry.  Pairing necklaces or matching voltages
without this phase is not the physical complement lift.

## 3. PBBS flags: one protected bank, not two

Let \((A_j)\) be a cycle in the odd graph \(O_m=KG(2m+1,m)\), and let

\[
 z_j=\Omega\setminus(A_j\cup A_{j+1})               \tag{3.1}
\]

be its missing-element edge label.  On an odd component, index its Middle
Levels lift by

\[
 T_i=\overline{A_{2i-1}},\qquad X_i=A_{2i}.         \tag{3.2}
\]

Then

\[
 e_i=z_{2i-1},\qquad a_i=z_{2i}.                    \tag{3.3}
\]

Put \(B_i=A_{2i}\) and

\[
 F_i^{(q)}=\bigcap_{h=0}^{q-1}B_{i+h}\qquad(q\ge1).\tag{3.4}
\]

Since \(X_i=T_i\cap T_{i+1}\), Theorem 1.1 gives the exact flag identity

\[
 \boxed{
 \overline{\bigcup_{h=0}^{q-1}T_{i+h}}
  =\bigcap_{h=0}^{q}T_{i+s+h}
  =\bigcap_{h=0}^{q-1}X_{i+s+h}
  =F_{i+s}^{(q)}.}                                  \tag{3.5}
\]

The audited PBBS all-depth theorem supplies, for every
\(R\in\binom{\Omega}{m-q}\), a consecutive \((q+1)\)-state \(B\)-path
with intersection \(R\).  Taking \(q+1\) in (3.5) therefore supplies the
complementary upper target \(\overline R\) at upper depth \(q\).  At
\(k=15\), for example, the \(5{,}005\) rank-six lower-\(q2\) targets are
exactly the complements of the \(5{,}005\) immediate upper targets.

### Corollary 3.1 (protected PBBS bank)

Suppose a downstairs PBBS fusion protects, for every lower target and every
required depth, one selected odd-graph flag interval: no selected interval
is cut, and its every-second state order remains consecutive (reversal is
allowed because intersection is unordered).  Then the complete lower flag
tower and its complementary upper tower both survive **as cyclic set
support**.  It is sufficient to protect the lower bank in the cyclic
construction; the upper bank is its deck transform.

For an odd base component the mate lies in the same lifted cycle.  For an
even base component it lies in the other lifted cycle.  After a linear
opening, the same conclusion requires the cut to avoid both the chosen
interval and its shifted deck mate: equivalently use antipodally paired cuts
on an odd lift, paired cuts on the two even lifts, or verify the mate
interval separately.  An unpaired upstairs cut does not satisfy the linear
version, even if the downstairs factor was complement closed.

This is a shadow-support statement.  It neither supplies a residence-safe
fusion nor preserves orientation-sensitive ports or pin addresses, and it
does not turn the selected occurrences into one owner-compatible compiler
assignment.

## 4. Exact odd/even lift theorem

The parity issue is most transparent for one physical odd-graph cycle

\[
 C=(A_0,A_1,\ldots,A_{L-1},A_0).                   \tag{4.1}
\]

Its canonical Middle Levels lift is the bipartite double cover: the two
vertices over \(A\) are the lower set \(A\) and the upper set
\(\overline A\), and complementation is the deck involution.

### Theorem 4.1 (component parity)

1. If \(L\) is odd, the double cover of \(C\) is one cycle of length
   \(2L\), and complementation is its half-turn.  With \(i\in\mathbb Z_L\),
   (3.2) gives its suppressed upper chronology and

   \[
    \overline{T_i}=X_{i+(L-1)/2}.                  \tag{4.2}
   \]

2. If \(L\) is even, the double cover splits into two cycles exchanged by
   complement.  With \(\epsilon\in\{0,1\}\) and
   \(i\in\mathbb Z_{L/2}\), write

   \[
    T_i^\epsilon=\overline{A_{\epsilon+2i-1}},
    \qquad X_i^\epsilon=A_{\epsilon+2i}.           \tag{4.3}
   \]

   The exact cross-component identities are

   \[
   \boxed{
    \overline{T_i^\epsilon}=X_{i+\epsilon-1}^{1-\epsilon},
    \qquad
    \overline{X_i^\epsilon}=T_{i+\epsilon}^{1-\epsilon}.}     \tag{4.4}
   \]

   Consequently, if

   \[
    U_i^{\epsilon,q}=\bigcup_{h=0}^{q}T_{i+h}^\epsilon,
    \qquad
    P_j^{\epsilon,q+1}=\bigcap_{a=0}^{q+1}T_{j-a}^\epsilon,
   \]

   then

   \[
    \boxed{
    \overline{U_i^{\epsilon,q}}
       =P_{i+\epsilon+q}^{1-\epsilon,q+1}.}         \tag{4.5}
   \]

#### Proof

Traversing one edge of the base cycle changes sheets in its bipartite
double cover.  The lifted walk closes after \(L\) steps precisely when
\(L\) is even; hence an even base cycle gives two \(L\)-cycles, whereas an
odd base cycle requires \(2L\) steps and gives one cycle.  The deck
involution exchanges the even pair and is the half-turn of the odd lift.

Formula (4.2) follows because
\(2(i+(L-1)/2)=2i-1\pmod L\).  Equations (4.4) follow directly by matching
the base indices in (4.3).  Complementing the union in (4.5), using the
first identity in (4.4), and replacing each \(X_j\) by
\(T_j\cap T_{j+1}\) gives the consecutive mate states from
\(i+\epsilon-1\) through \(i+\epsilon+q\), which is the displayed backward
erosion.  \(\square\)

### Example 4.2 (minimal even-component obstruction)

In \(O_2\), consider the even cycle

\[
 12,34,15,23,14,35,12.                              \tag{4.6}
\]

Its two suppressed upper lifts are

\[
 (124,125,145),\qquad (345,234,235).                \tag{4.7}
\]

Complementation exchanges them.  Explicitly,

\[
 \overline{124\cup125}=\{3\}=345\cap234\cap235,   \tag{4.8}
\]

whereas the corresponding threefold intersection in the first component is
\(124\cap125\cap145=\{1\}\).  Thus same-component complement halving is
false on an even component; only the paired-factor statement survives.

## 5. Rotation quotient and run-transversal transport

Let a directed quotient cycle of length \(n\) in \(O_m/\langle\rho\rangle\)
have voltage \(v\in\mathbb Z_k^\times\).  Number its physical lift by

\[
 A_{j+n}=\rho^vA_j.                                  \tag{5.1}
\]

It has length \(kn\).  Since \(k\) is odd, its parity is the parity of
\(n\).

### Theorem 5.1 (unit-voltage transport)

If \(n\) is odd, the single lifted upper chronology satisfies

\[
 \boxed{T_{i+n}=\rho^{2v}T_i.}                      \tag{5.2}
\]

If \(n\) is even, each of the two upper components satisfies

\[
 \boxed{T_{i+n/2}^\epsilon=\rho^vT_i^\epsilon.}     \tag{5.3}
\]

In either case the displayed voltage is a unit.  After conjugating
coordinates so that the voltage is one, the component has a binary trace
\(c\).  Its rank and Johnson seam equations force exactly one `01` boundary
and one `10` boundary in every residue class of the quotient period.
Equivalently, the cyclic one-run starts and ends are both residue
transversals.

#### Proof

For odd \(n\), equations (3.2) and (5.1) give

\[
 T_{i+n}=\overline{A_{2i+2n-1}}=\rho^{2v}T_i.
\]

For even \(n\), (4.3) gives

\[
 T_{i+n/2}^\epsilon
 =\overline{A_{\epsilon+2i+n-1}}=\rho^vT_i^\epsilon.
\]

Multiplication of coordinate labels by the inverse voltage gauges either
relation to \(T_{i+N_0}=\rho T_i\), where \(N_0\) is the relevant quotient
period.  Define \(c_j={\bf1}_{\{0\in T_j\}}\).  Equivariance gives

\[
 T_i=\{x:c_{i-xN_0}=1\}.
\]

The rank equation gives the correct class sum in each residue.  At seam
\(i\), entering coordinates are precisely the `01` boundaries whose left
index is congruent to \(i\pmod {N_0}\), and leaving coordinates are the
`10` boundaries in that residue.  Johnson adjacency gives exactly one of
each.  These are precisely the run-start and run-end transversals.
\(\square\)

### Corollary 5.2 (the exact PBBS fusion target)

A rotation-equivariant downstairs PBBS fusion to one quotient cycle of odd
total length and unit voltage automatically yields one internally
complement-coherent, run-transversal Middle Levels carrier.  At \(k=15\),
the full quotient length is

\[
 \operatorname{Cat}_7=429,
\]

which is odd.  Therefore the additional conditions needed from such a
fusion are exactly:

1. preservation of one selected PBBS lower flag witness per required
   target/depth (the upper bank then follows from Section 3);
2. the physical short-return/residence conditions at all new seams; and
3. whatever common-owner/compiler conditions are required after chronology.

An arbitrary physical or upstairs join need not be rotation-equivariant and
therefore need not admit one scalar `c`-word.  Complement closure by itself
does not repair this.

Parity also constrains component fusion downstairs.  The self-antipodal
property depends on the parity of the total quotient length: even plus even
and odd plus odd remain complement-exchanged, while odd plus even becomes
self-antipodal.  A final quotient Hamilton cycle at \(k=15\) has the needed
odd parity.

Run transversality is still weaker than residence.  The explicit PBBS
quotient three-cycle in `PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`,
Theorem 8.2, has unit voltage and hence satisfies Theorem 5.1, but its
physical component has \(\nu_3\ge m\) edge-disjoint short-return intervals.
Thus neither unit voltage nor the two run-boundary transversals eliminates
the depth-three residence obstruction.

## 6. The inverse-two NAND order is not a lift

For an odd complement-coherent carrier, the scalar normal form introduces

\[
 d_j=c_{tj},\qquad t=2^{-1}\pmod W,                 \tag{6.1}
\]

so that the NAND law becomes local in the \(d\)-order.  This is an
algebraic permutation of trace positions, not a chronology-preserving
operation.

Indeed, write \(W=kC\).  The local NAND constraints make every zero of
\(d\) isolated, and the class totals give exactly \(mC\) zeros.  Hence
\(d\) has exactly \(mC\) cyclic one-runs.  The physical complement law and
the same class totals force exactly \(C\) cyclic one-runs in \(c\), as does
run transversality modulo \(C\).  For \(m>1\),

\[
 mC\ne C.                                           \tag{6.2}
\]

Therefore \(d\) cannot itself be the transported run-transversal carrier.
The legitimate odd/even transport is the incidence lift of Sections 4--5,
with deletion labels \(z_{2i-1}\) and insertion labels \(z_{2i}\); scalar
decimation destroys physical adjacency and residence.

## 7. Exact remaining boundary

The proved implication is:

> **Equivariant protected-fusion theorem (conditional input).**  If a
> rotation-orbit PBBS switch sequence produces one odd, unit-voltage
> quotient cycle, preserves one selected lower PBBS flag interval for every
> required target/depth, and satisfies the new-seam residence tests, then
> its Middle Levels lift is a complement-coherent run-transversal carrier
> with complete lower and upper flag support.  Only the lower witness bank
> must be protected.

Every implication in this statement is proved above.  What is not proved is
the existence of the stated switch sequence.  The smallest surviving
hypothesis is therefore not a second upper decoration system: it is an
equivariant unit-voltage PBBS fusion that simultaneously avoids one chosen
lower witness bank and all forbidden short-return collars.  Owner/compiler
compatibility remains subsequent and independent.

## 8. Audit trail

The argument was checked independently in three ways.

1. Direct De Morgan and seam indexing gives the forward identity (1.5) and
   the backward terminal \(i+s+q+1\) in (1.13).
2. Coordinatewise substitution in the scalar NAND law gives the independent
   clock identity (2.5).
3. The even \(O_2\) cycle (4.6) verifies that the complement target lies in
   the mate component and explicitly falsifies the tempting same-component
   version.

The main hidden-boundary risks are thereby resolved: `+1` depth, terminal
index, quotient carry, even-component pairing, physical versus permuted
scalar order, and cyclic versus linear endpoint protection.
