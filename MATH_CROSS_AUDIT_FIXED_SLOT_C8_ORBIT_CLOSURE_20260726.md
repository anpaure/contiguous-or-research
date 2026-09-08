# Cross-audit of the fixed-slot reciprocal-\(C_8\) cube and its physical orbit closure

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Let \(D_s\) be the Dyck words of length \(2s\), and put

\[
                         B=C_s=\operatorname {Cat}_s.
\]

Fix pairwise disjoint four-coordinate slots.  At a slot beginning after
\(t\) bits, interchange

\[
                     U1100V\longleftrightarrow U1010V,
                     \qquad |U|=t.                    \tag{0.1}
\]

The fixed-slot bypass is valid, including at positive height.

1. Every fixed slot supports exactly \(C_{s-2}\) sealed reciprocal
   \(C_8\)'s.  The prefix before the slot need not be a Dyck word.
2. Disjoint slots have disjoint MSW chronology slabs.  Their packet
   transformations commute even when their root supports overlap.
3. The full ownership components are the Boolean root cubes.  For \(u\)
   slots the all-on edit moment is exactly
   \[
   \boxed{
   \Xi_u={4\over C_s}\sum_{h=1}^u
          \binom uh h2^hC_{s-2h}}
   ={u\over2}\left({9\over8}\right)^{u-1}+O_u(s^{-1}). \tag{0.2}
   \]
   Hence every fixed \(4\le u\le7\) has \(\Xi_u=O_u(1)=o(\sqrt s)\).

Thus the earlier \(C_{s-1}\) inventory ceiling is not a ceiling for this
construction.  It counted root-disjoint packets occurring after complete
top-level Dyck prefixes.  The present packets include positive-height
gaps and, more importantly, satisfy a separately proved cubical face
identity on shared roots.  The old root-disjoint theorem remains true on
its stated domain, but its inventory conclusion cannot be applied here.

The stronger physical conclusion is also valid.  If the slots begin in
odd physical positions, every packet is a rowwise image under a generator
of

\[
 H_s=\langle(2\ 3),(4\ 5),\ldots,(2s-2\ 2s-1)\rangle. \tag{0.3}
\]

Consequently the complete target mass on every \(H_s\)-orbit is invariant
at each rank.  This is an identity for the actual simultaneous factor; it
already contains all collars and mixed-window terms.  In the standard
one-step parent, the singleton orbit \(\{2,3\}\) contains distinguished
canonical occurrence families of sizes

\[
                              C_s,\qquad C_{s-1}.     \tag{0.4}
\]

Therefore every legal fixed-slot cube state satisfies, for
\(p=C_s/\theta\) and \(4\le\theta<16\),

\[
 \boxed{
  (\mu(2)-p)_++(\mu(3)-p)_+
   \ge C_s+C_{s-1}-2p
   \ge {1\over2}C_s.}                                \tag{0.5}
\]

The tagged supply \(uC_{s-2}\) is real, but it cannot repair the canonical
physical PCap gate.  The exact redirect is a non-coordinate packet which
transfers mass between distinct target orbits while retaining fixed ports,
exact ownership, and \(\Xi=o(\sqrt s)\).

## 1. Positive-height slots are literal MSW rectangles

Let \(R\in D_{s-2}\), mark any one of its \(2s-3\) gaps, and insert

\[
                         d_0=1100,
              \qquad    d_1=1010.                    \tag{1.1}
\]

Both are nonnegative excursions of net height zero.  Inserting either at
any gap preserves every Dyck prefix inequality.  Deleting the displayed
block is the inverse operation.  Hence a fixed slot has \(2C_{s-2}\)
eligible roots, paired into \(C_{s-2}\) root edges.

The remaining point is MSW chronology, not Dyck legality.  Write
\(\mu\) for reverse-complement.  The MSW recursion is

\[
 \rho(1a0b)=
 \bigl(|a|+2,\ |a|+2-\rho(\mu a),\ 1,
                    |a|+2+\rho(b)\bigr).             \tag{1.2}
\]

### Lemma 1.1 (one-hole localization)

For either insertion in (1.1), the four inserted labels occupy one
consecutive block of the MSW order.  The order outside that block is the
same for \(d_0\) and \(d_1\).  Inside the block the two orders are, after
one common affine relabelling and possibly reversal,

\[
 \rho(d_0)=(4,2,3,1),
 \qquad
 \rho(d_1)=(2,1,4,3).                                \tag{1.3}
\]

The affine relabelling sends the local middle pair \(\{2,3\}\) to the
two middle physical coordinates of the slot.

#### Proof

Induct on the semilength of the erased word \(R\).  In its first-return
decomposition \(R=1a0b\), the marked gap is either in \(a\), in \(b\),
or between primitive components.

If it is in \(b\), the last block of (1.2) applies the induction
hypothesis followed by a common shift.  If it is in \(a\), reverse-
complement reflects the marked gap inside \(\mu a\); induction followed
by the affine reversal in the second block of (1.2) again leaves one
consecutive four-label block.  A gap between primitive components is the
concatenation case

\[
                         \rho(PQ)=(\rho(P),|P|+\rho(Q)). \tag{1.4}
\]

These cases include the endpoint gaps.  Finally
\(\mu d_0=d_0\) and \(\mu d_1=d_1\), so reflection does not change the
two local words.  It only reverses the common embedding of their four
labels.  The central pair remains the central physical pair. \(\square\)

Let those four physical labels be
\(\alpha,\beta,\gamma,\delta\), in the induced order.  Cyclically move
the common exterior behind the local block.  The two old orders and their
middle-pair transposes are

\[
\begin{aligned}
 C&=(\delta,\beta,\gamma,\alpha,T),
 &D&=(\beta,\alpha,\delta,\gamma,T),\\
 C'&=(\delta,\gamma,\beta,\alpha,T),
 &D'&=(\gamma,\alpha,\delta,\beta,T).
\end{aligned}                                         \tag{1.5}
\]

The standard four-cut table is independent of the common tail \(T\):
the two old rows and the two new rows own the same six middle states and
the same four adjacent-union colours.  Their ports agree.  Thus (1.5) is
a sealed reciprocal \(C_8\) in every one-hole context.

Equivalently, if \(\tau=(\beta\ \gamma)\), then on the two packet roots
\(P,\tau P\) the alternative rows satisfy the full ambient identity

\[
 \omega_{\operatorname{new}}(P)=\tau\omega_{\operatorname{old}}(\tau P),
 \qquad
 \omega_{\operatorname{new}}(\tau P)
   =\tau\omega_{\operatorname{old}}(P).              \tag{1.6}
\]

This identity is the point needed later for the physical carrier.  It is
not merely a local signed-ledger equality.

## 2. Disjoint-slot tensorization and exact accounting

Let \(I_1,\ldots,I_u\) be disjoint slots and let \(\tau_j\) be the
middle-pair transposition in slot \(j\).  For a root \(x\), put

\[
 J(x)=\{j:x|_{I_j}\in\{1100,1010\}\}.                \tag{2.1}
\]

The maps \(\tau_i,\tau_j\) inspect and change disjoint bit positions.
Thus they commute and preserve \(J(x)\).  Lemma 1.1 gives more: in the
ambient MSW order, each toggle changes only its own consecutive
four-label block.  The corresponding Johnson-path slabs have disjoint
interiors and fixed boundary states.

For a mask \(A\subseteq[u]\), define

\[
 h_{A,x}=\prod_{j\in A\cap J(x)}\tau_j,
 \qquad
 F^A(x)=h_{A,x}F_s(h_{A,x}x).                         \tag{2.2}
\]

### Theorem 2.1 (exact cubical composition)

Every \(F^A\) is an anchored exact factor.  The order of the slot
operations is irrelevant.

#### Proof

For one slot, (1.5) is a sealed two-row equality.  Suppose some disjoint
slots have already been installed.  On a pair \(x,\tau_jx\), all earlier
operations apply the same common conjugation \(h\), supported away from
the \(j\)-slot.  Conjugating the complete equality (1.5) by \(h\) leaves
another sealed equality.  Its chronology slab is disjoint from all earlier
slabs, so the row gluing states are unchanged.  Induction proves (2.2),
both ownership ledgers, and the fixed root/complement ports. \(\square\)

For any prescribed \(h\) slots, simultaneous deletion and reinsertion
give the exact count

\[
 \#\{x:\text{all prescribed slots are eligible}\}
                         =2^hC_{s-2h}.                \tag{2.3}
\]

Hence the root orbit of \(x\) is the Boolean cube

\[
                  \{\tau_Tx:T\subseteq J(x)\}.       \tag{2.4}
\]

No ownership edge leaves (2.4), while the transferred token in every
local \(C_8\) supplies every coordinate edge.  Thus (2.4) is exactly one
full ownership component, of side size \(2^{|J(x)|}\).

Each active slot changes one middle state of the rooted Johnson path.  In
the rooted coordinate order this is one adjacent transposition in the
deletion list and one in the insertion list, so

\[
                             d(x)=2|J(x)|.             \tag{2.5}
\]

With

\[
 Z_u(z)=\sum_{x\in D_s}z^{|J(x)|},
\]

the identity \(z^{|J|}=\sum_{T\subseteq J}(z-1)^{|T|}\) and (2.3) give

\[
 Z_u(z)=\sum_{h=0}^u\binom uh
                  \bigl(2(z-1)\bigr)^hC_{s-2h}.      \tag{2.6}
\]

Weighting (2.5) by the component size gives

\[
 C_s\Xi_u=\sum_x2^{|J(x)|}\,2|J(x)|=4Z_u'(2),        \tag{2.7}
\]

which proves (0.2).  Since
\(C_{s-2h}/C_s=16^{-h}(1+O_h(s^{-1}))\), the displayed asymptotic has
its stated error.

This is precisely the joint recombination that was missing from the old
root-disjoint packet theorem.  Root overlap is not being ignored; it is
resolved by the common row carrying all of its disjoint slab changes.

## 3. Full physical target-orbit invariance

For a rooted coordinate order \(\omega\) and a pointed start \(r\), let
\(\Gamma_q(\omega,r)\) be its complete rank-\(q\) physical target,
including the literal exterior collar.  Coordinate permutations commute
with intersection, union, complement, and adjoining a collar.  Extending
a local permutation by the identity outside the child coordinates gives

\[
                 \Gamma_q(\sigma\omega,r)
                    =\sigma\Gamma_q(\omega,r).        \tag{3.1}
\]

Let \(\Gamma_{\mathcal I}=\langle\tau_j:1\le j\le u\rangle\).  For
odd-start slots, \(\Gamma_{\mathcal I}\le H_s\).

### Theorem 3.1 (orbit closure, including mixed windows)

At every protected rank, every legal factor produced by the disjoint-slot
cube has the same total physical target mass as the canonical factor on
each \(\Gamma_{\mathcal I}\)-orbit.  For odd-start slots the same is true
on each \(H_s\)-orbit.

#### Proof

Consider one current packet on roots \(P,\tau_jP\).  Equation (1.6),
with any already installed disjoint conjugation included on both rows,
gives a start-preserving bijection from its old pointed occurrences to
its new pointed occurrences.  By (3.1), every new target is the
\(\tau_j\)-image of its old partner.  Thus the packet preserves the total
on every orbit of a group containing \(\tau_j\).

Install the legal packet directions sequentially and sum this identity.
This proves the assertion for \(\Gamma_{\mathcal I}\).  If all generators
belong to \(H_s\), the same argument with the coarser \(H_s\)-orbits proves
the second assertion.

Equivalently, this can be checked directly for componentwise cube
choices.  On one root cube \(K\), a chosen mask \(A_K\) gives one fixed
\(h_K\in\Gamma_{\mathcal I}\), and (2.2), followed by the reindexing
\(y=h_Kx\), gives

\[
 \sum_{x\in K}{\cal M}_q(F^{A_K}(x))
   =(h_K)_*\sum_{y\in K}{\cal M}_q(F_s(y)),           \tag{3.2}
\]

where \({\cal M}_q\) is the complete pointed-target multiset.  Thus the
identity remains true when different full ownership components choose
different legal masks. \(\square\)

No isolated-column expansion was used.  A window whose two boundaries
meet two different switched slabs is transported as part of the actual
final row.  Therefore every quadratic mixed-window term is already
included in Theorem 3.1 and cannot leak mass between target orbits.

There is one necessary wording qualification.  A geometrically named
start subfamily need not be fixed under the reanchoring
\(P\leftrightarrow\tau_jP\).  The theorem applies to the full physical
histogram, or to a marked family transported through the occurrence
bijection.  It must not be asserted for an untransported root/start name.

## 4. The fatal two-cell orbit

In the standard one-step parent, the first-return boundary census is

\[
                   w_j=C_{j-1}C_{s+1-j},
                   \qquad1\le j\le s+1.              \tag{4.1}
\]

The even boundary copy of class \(j\) has local target \(2j\), and the
odd copy has local target \(2j-1\).  Taking the first two relevant classes
gives distinct occurrence families

\[
                 \mu^\circ(2)=w_1=C_s,
        \qquad   \mu^\circ(3)=w_2=C_{s-1}.            \tag{4.2}
\]

Transport these two marked families through the bijections in Theorem
3.1.  They remain distinct occurrences.  For odd-start slots their
targets remain in the singleton \(H_s\)-orbit \(\{2,3\}\).  Since all
other physical occurrences have nonnegative multiplicity,

\[
                         \mu(2)+\mu(3)
                              \ge C_s+C_{s-1}.         \tag{4.3}
\]

If the two marked families exhaust the initial singleton-orbit load,
Theorem 3.1 gives equality; the lower bound is all that is needed.

For \(p=C_s/\theta\), convexity gives

\[
\begin{aligned}
 (\mu(2)-p)_++(\mu(3)-p)_+
 &\ge\mu(2)+\mu(3)-2p\\
 &\ge C_s+C_{s-1}-{2C_s\over\theta}\\
 &=C_s\left(1+{s+1\over2(2s-1)}-{2\over\theta}\right).
\end{aligned}                                         \tag{4.4}
\]

For \(\theta\ge4\), the last expression is at least
\(C_s/2+C_{s-1}>C_s/2\).  This proves (0.5), uniformly throughout the
fatal range \(4\le\theta<16\).

The same argument can be stated without the odd-start restriction.  For
arbitrary disjoint slots use \(\Gamma_{\mathcal I}\).  If the first slot
is absent, no active middle pair contains coordinate \(2\), so the
singleton target \(2\) retains at least \(C_s\) mass and contributes
\(C_s-p\).  If the first slot is present, disjointness isolates its pair
\(\{2,3\}\), and (4.4) applies.  Thus every disjoint fixed-slot atlas,
not only the coherently tagged odd-start choice, leaves \(\Omega(C_s)\)
physical excess.

## 5. Exact proved boundary

The audit yields a split positive/negative theorem.

* Positive: positive-height fixed slots are certified reciprocal
  \(C_8\)'s; disjoint slots tensor exactly on shared root cubes; their
  component sizes are bounded for fixed \(u\); and (0.2) gives the exact
  sparse-edit moment.
* Negative: every such packet is a coordinate image, so the full physical
  target histogram is trapped in coordinate-group orbit sums.  The
  canonical fatal singleton orbit retains the quantitative excess (0.5),
  even after collars, target collisions, and mixed-window interactions.

The former common-base inventory objection is therefore superseded, but
the proposed coefficient-one repair is still closed.  A viable successor
must change the orbit module itself: at least one packet must move physical
mass between distinct \(H_s\)-orbits (or change the exported parent
boundary profile) while preserving exact \(X/Y\) ownership and the
\(o(\sqrt s)\) edit threshold.

No constant-one conclusion is claimed.
