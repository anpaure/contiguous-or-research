# The zero-defect Pascal package is reversal-closed; only relative socket alignment survives

**Date:** 2026-08-01  
**Lane:** same-parity Pascal/PBBS induction modulo global reversal  
**Status:** exact field-by-field state audit, exact particle involution, and
exact conditional \(B+O(1)\)/equality implication.  The joint protected
host, absolute opening compensation, one-phase terminal compiler, and
regeneration remain unproved.

## 0. Verdict

The zero-defect scalar/palette package of
`MATH_THEOREM_ZERO_DEFECT_PASCAL_PARTICLE_BRAID_INDUCTION_20260731.md`
does not contain an absolute orientation.

Every named field is either:

1. fixed by reversal;
2. exchanged with its left/right mate; or
3. transported to a reflected occurrence address.

The particle thresholds have the exact involution

\[
 \boxed{
 G_t^*=W-H_{d-1-t},\qquad H_t^*=W-G_{d-1-t}.}              \tag{0.1}
\]

It preserves chain alignment, residence feasibility, nonempty envelopes,
and the exact loss.  A shallow prefix staircase becomes a shallow suffix
staircase; the two are one quotient state.

The known one-sided split-core recurrence also closes after adjoining its
reflection.  Its packet prefix, terminal right nonowner, right suffix word,
gap schedule and terminal cap all move together to the opposite side.  Thus
there is no isolated absolute left/right obstruction in that local
transducer.

The sole possible orientation obstruction is **relative**:

\[
 \boxed{\text{two independently rooted sockets may demand opposite choices
 which global reversal flips simultaneously.}}              \tag{0.2}
\]

For example, a Pascal root facet stored at one endpoint and an independently
named packet socket have a same-side/opposite-side bit.  Reversal does not
change that bit.  In the odd B1 state this obstruction vanishes because the
missing q1 colour lies in both endpoints and can root either orientation.
In a multi-component trace system the analogous component-relative bits must
be retained explicitly.

Accordingly the complete-reversal role converter can be deleted from the
existential same-parity induction target.  The remaining theorem asks for
one oriented protected child, not two phases with a common fixed-address
compiler.

## 1. Reversal of the particle schedule

Use the normal form of the deadline-staircase theorem.  A word has physical
length

\[
                              L=W+d.                         \tag{1.1}
\]

Let

\[
 X=\{x_0<\cdots<x_{d-1}\},\qquad
 Y=\{y_0<\cdots<y_{d-1}\}                                 \tag{1.2}
\]

be the omitted starts and omitted deadlines, and put

\[
                              G_t=x_t-t,\qquad H_t=y_t-t.    \tag{1.3}
\]

Reflect physical positions by \(p\mapsto L-1-p\).  Starts and deadlines
exchange, so the reflected omitted sets are

\[
 x_t^*=L-1-y_{d-1-t},\qquad
 y_t^*=L-1-x_{d-1-t}.                                      \tag{1.4}
\]

### Theorem 1.1 (exact particle involution)

The reflected thresholds are (0.1).  They are nondecreasing and satisfy

\[
                              (G^*,H^*)^*=(G,H).             \tag{1.5}
\]

Moreover,

\[
                 \operatorname{Loss}(G^*,H^*)
                   =\operatorname{Loss}(G,H).               \tag{1.6}
\]

Nonempty support, chain alignment, every coordinate residence corridor,
and maximal-envelope nonemptiness hold for \((G,H,T)\) if and only if they
hold for \((G^*,H^*,\operatorname{rev}T)\).

#### Proof

Substitute \(y_{d-1-t}=H_{d-1-t}+d-1-t\) into (1.4):

\[
 G_t^*=L-1-y_{d-1-t}-t=W-H_{d-1-t}.
\]

The formula for \(H_t^*\) is identical.  Monotonicity and (1.5) follow
immediately.

For the exact loss,

\[
\begin{aligned}
 \sum_tH_t^*&=dW-\sum_tG_t,\\
 \sum_t(W-G_t^*)&=\sum_tH_t,
\end{aligned}                                               \tag{1.7}
\]

and

\[
 \#\{(t,u):G_t^*<H_u^*\}
   =\#\{(v,s):G_v<H_s\}.                                   \tag{1.8}
\]

Equations (1.7)--(1.8) prove (1.6).  Reflecting every selected owner interval
interchanges its start and deadline.  It therefore preserves support
nonemptiness and chain alignment.  Coordinate runs and maximal envelopes
are reflected intervals, proving the remaining assertions. \(\square\)

### Corollary 1.2 (the special one-jump state)

A staircase whose short rows form a prefix of length \(a\) reflects to one
whose short rows form a suffix of length \(a\).  These have the same scalar
capacity and residence status.  The one-jump theorem written with a short
prefix is therefore a canonical representative theorem, not an absolute
orientation restriction.

For the k=17 terminal-start calibration

\[
                         G=(W,W,W),\qquad H=(0,0,7401),       \tag{1.9}
\]

the reflected schedule is

\[
                         G^*=(W-7401,W,W),\qquad H^*=(0,0,0). \tag{1.10}
\]

It is generally not another terminal-start schedule.  Thus a theorem which
artificially restricts both representatives to \(G=(W,\ldots,W)\) is not
reversal-closed.  The corrected quotient class contains the terminal-start
normal form and its reflected early-start normal form.

## 2. Complete field audit of the zero-defect package

The following table uses the four clauses of the exact zero-defect induction
theorem.

| field | reversal action | quotient status |
|---|---|---|
| scalars \(W,\Lambda,d,D,\sigma,\Gamma\) | fixed | closed |
| middle chronology \(T_0,\ldots,T_{W-1}\) | reverse order | closed |
| rank and owner multiplicities | fixed | closed |
| upper witness interval \([i,j]\) | \([L-1-j,L-1-i]\) | closed |
| odd q1 hole \(h\) | same set; endpoints swap | B1 is fixed |
| even q1 hole/excess ledger \((H,E,J)\) | fixed | closed |
| path-cover components | reverse each path and reverse their global order | closed as an unordered cover |
| cuts and seam colours | same set-valued colours; endpoint roles swap | closed |
| sectors \(A,U,X,Y\) | \(A,U\) fixed; \(X,Y\) swap with the new coordinates | closed under \(x\leftrightarrow y\) |
| socket bits \((\alpha_i,\beta_i)\) | swap after index reflection | closed |
| particle thresholds \((G,H)\) | (0.1) | closed by Theorem 1.1 |
| maximal envelope \(E_p\) | \(E_{L-1-p}\) | closed |
| pin \((S,[i,j])\) | \((S,[L-1-j,L-1-i])\) | closed |
| cap/source letter at \(p\) | same set at \(L-1-p\) | closed |
| common-cap matching \(\mu\) | reflect every cell address | closed; no phase intersection needed |
| protected flag occurrence | same nested values at reflected root address | closed |
| carried target sidecar | target values fixed; witness addresses reflect | closed |

The signed endpoint profiles require one qualification.  A left clipped run
of length \(a\) becomes a right clipped run of length \(a\).  Therefore the
state must store the ordered pair only up to

\[
                              (\ell,r)\sim(r,\ell).            \tag{2.1}
\]

The scalar/palette recurrences themselves already obey this symmetry.

### Theorem 2.1 (zero-defect package is reversal-equivariant)

If an oriented occurrence-labelled child satisfies Clauses 1--4 of the
zero-defect Pascal particle-braid theorem, then its reflected child also
satisfies Clauses 1--4, with exactly the same particle loss and the reflected
compiler matching.

#### Proof

Owner and upper closure transport by interval reflection.  The q1 ledger is
an edge-colour multiset and is unchanged.  Theorem 1.1 transports Clause 3.
The cap equations are unions and intersections over reflected intervals, so
reflecting every pin and compiler edge transports Clause 4. \(\square\)

This removes a former overconstraint: a regenerative quotient package needs
one terminal common-cap solution, not one matching contained in the
fixed-address intersection of two phase graphs.

## 3. Facet/Pascal trace fields

The dimension-uniform facet recurrence adds three apparent orientation
choices.

### 3.1 Cycle traces

Reversing a Pascal cycle trace reverses its facet trace, up to a cyclic index
shift.  Hence the vertex/facet middle partition and the shadow-shift identity
are exactly invariant.

### 3.2 Rooted path traces

A general rooted path stores one facet only at its first endpoint.  After
reversal that occurrence is a facet at the terminal endpoint, so the
oriented definition is not literally closed.  The minimal quotient datum is

\[
    (\text{path},\ \text{one declared root facet},\
      \text{the endpoint carrying it})/\text{reflection}.     \tag{3.1}
\]

For a path obtained by opening a q1-rainbow cycle, the deleted colour is
contained in **both** exposed owners.  In particular, every odd B1 path has
a bi-end root facet.  On that face (3.1) has no residual orientation bit.

If an arbitrary path is not known to come from such an opening, the next
facet lift must either retain a root facet at each possible endpoint or keep
the endpoint choice as real state.

### 3.3 The hinge singleton

The top-singleton socket at the cap/facet hinge reflects to the opposite
hinge and has the same singleton value.  It is one-sided only in the chosen
normal form.  A theorem which supplies it at the shallow-prefix hinge has a
reflected shallow-suffix version automatically.

## 4. Audit of the one-sided split-core recurrence

The inherited split-core state records:

1. an initial protected packet;
2. a terminal nonowner \(a\) at the opposite end;
3. the packet's exterior-facing suffix word \(\omega_h\);
4. one right gap schedule \(\Gamma_h\);
5. a terminal source word \(\theta_h\);
6. two cap/repair choices and their alternate singleton hosts; and
7. the shared-coordinate birth-depth ledger.

Under reversal, items 1--5 all exchange sides together, the two cap choices
swap, and the birth ledger is fixed.  The no-jump and jump formulas reflect
word-for-word after

\[
                              \alpha\longleftrightarrow\gamma. \tag{4.1}
\]

### Theorem 4.1 (local quotient-totality)

Adjoin to the stated right-oriented split-core transducer its literal
reflection.  Every orbit of a locally admissible split-core state then has
one representative to which the transducer applies, and the output is again
one such orbit.

Thus the packet-prefix/terminal-right convention is not an obstruction to
quotient induction.

#### Proof

The displayed parent-to-child equations use only ordered concatenation,
union, and the two fresh labels.  Reverse every concatenation and apply
(4.1).  This yields the reflected transducer.  The seven state fields above
all move with the same orientation bit. \(\square\)

This closes only the **local algebraic** recurrence.  Its shared-bank
residence horizon and global exterior/common-cap hypotheses remain exactly
as before.

## 5. The minimal one-sided obstruction is a relative bit

Let a state contain two oriented sockets \(s_1,s_2\), each carried by one
of the two global endpoints.  Encode their endpoint choices by
\(\epsilon_1,\epsilon_2\in\mathbb F_2\).  Global reversal adds one to both,
so

\[
                         \epsilon_1+\epsilon_2               \tag{5.1}
\]

is invariant.

### Theorem 5.1 (minimal relative-socket obstruction)

A one-sided transition normal form is total on reversal orbits if and only
if every required socket alignment depends only on the one common orientation
bit, or the transition accepts every surviving relative bit such as (5.1).

The smallest failure is two sockets for which the host theorem requires
\(\epsilon_1=\epsilon_2\) while the supplied state has
\(\epsilon_1\ne\epsilon_2\), or conversely.  Reversal cannot repair it.

#### Proof

For one socket the two endpoint choices form one reversal orbit.  For two,
the four choices split into the two orbits classified by (5.1).  This is
both necessary and sufficient. \(\square\)

Concrete manifestations are:

* a Pascal root facet and an independently named packet socket;
* two separately oriented trace components;
* a terminal nonowner required at one end and a cap hinge independently
  required at an incompatible end; or
* two packet phases which a connector requires to be equal/opposite.

The currently stated split-core fields are synchronized and therefore do
not realize this obstruction.  The odd B1 root facet is available at both
ends.  A future global host theorem must nevertheless state the relative
alignment of every additional component socket; marginal left/right
availability is insufficient.

## 6. Exact quotient implication for equality and additive constant

Call a reversal orbit a **complete \(C\)-state** if it contains an oriented
representative with:

1. one occurrence of every middle owner and chosen witnesses for every
   upper target outside a sidecar \(Z\), \(|Z|\le C\);
2. the parity-correct q1 ledger, with every residual q1 hole included in
   \(Z\);
3. a legal nonempty particle staircase satisfying the exact scalar budget;
4. one occurrence-labelled terminal compiler covering every lower target
   outside \(Z\); and
5. every root facet, endpoint profile, protected flag, cap hinge and socket
   needed by the next step, recorded up to global reflection, with all
   relative alignment bits explicit.

### Theorem 6.1 (reversal-quotient regenerative implication)

Suppose there is an absolute \(C\), one complete base orbit in each parity,
and for every sufficiently large same-parity step a transition which maps
every complete \(C\)-orbit to another complete \(C\)-orbit.  Then

\[
                              \nu(k)\le B(k)+C               \tag{6.1}
\]

in all subsequent dimensions.  If \(C=0\), then

\[
                              \nu(k)=B(k).                   \tag{6.2}
\]

#### Proof

Choose at every step the representative accepted by the transition.  The
field audit and Theorem 1.1 show that choosing the other representative
would give the reflected child orbit with the same debt.  At the terminal
dimension, append the at most \(C\) literal masks in \(Z\).  This represents
them without destroying any existing interval.  The constructed word has
length at most \(B(k)+C\).  For \(C=0\), combine with the general lower
bound. \(\square\)

The sidecar is paid only at the terminal dimension, not at every transition.

## 7. The shortest remaining theorem

After quotienting by reversal, a proof of \(B(k)+O(1)\) needs exactly the
following rows in **one orientation**:

1. **protected owner/upper host:** a coefficient-one middle chronology with
   every arbitrary-width upper target covered except \(O(1)\) named targets;
2. **particle geometry:** thresholds \((G,H)\) with nonempty envelopes and
   exact loss within the scalar budget;
3. **absolute opening compensation:** ambient witnesses for all but \(O(1)\)
   targets lost by the chosen linear cuts;
4. **one-phase terminal cap:** one compiler matching leaving at most \(O(1)\)
   lower targets, not a common fixed-address matching of two phases;
5. **bounded regeneration:** the output carries the same quotient interface,
   with every relative socket bit explicitly accepted and sidecar size still
   \(O(1)\).

For exact equality replace every \(O(1)\) by zero and use the exact scalar
slack.

The scalar recurrence, palette Euler law, particle reflection, local
split-core transducer, and complete-reversal packet already satisfy the
quotient requirements.  The transition relation is **not yet proved total**
because Rows 1, 3, 4 and 5 remain open globally.  This failure is not an
absolute left/right socket: it is the nonexistence, so far, of the correlated
protected host and compiler in either orientation.
