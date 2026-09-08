# Address transport and the exact lower-C8 sidecar for the folded comparator

Date: 2026-08-01  
Lane: R, quotient-folded C8 physical comparator  
Status: unconditional occurrence-transport lemma and unconditional all-`d`
owner/`q1` sidecar.  The existing owner-legal basis-changing host does not
inherit the common-cut graded cancellation.  A protected ambient splice is
still unproved.

## 0. Verdict

Three facts settle the attempted direct composition.

1. Equal graded occurrence counters do give an explicit address transport,
   provided the whole affected address bank is mobile: pair, separately in
   every `(width,target)` bucket, the old addresses with the new addresses.
   This transports every matching injectively.  It is weaker than equality
   at the same address and it does not respect a frozen background unless the
   bucket equality holds separately on the frozen and mobile banks.
2. The two lower-boundary colours of the common coatom rail have an exact
   phase-dependent alternating `C8` sidecar.  It uses eight distinct rank-`r`
   owners, changes four edges to four edges, cancels the complete two-colour
   lower discrepancy, and has identical upper-`q1` counters in both phases.
   Thus the lower-palette obstruction is not an invariant once a non-common
   owner circuit is allowed.
3. This does **not** combine the two existing physical packets as written.
   Replacing the non-owner-simple plateau host in the canonical common-cut
   word by the owner-legal basis-changing word leaves an exact graded residue
   of `L1=6d-4`.  Therefore no bijection preserving `(width,target)` can
   exist for that direct substitution.  Independently, the common coatom
   rail uses `2d+1` source letters and still needs its two ambient halo
   identifications.

The smallest additional owner-palette datum is now explicit: one occurrence
of the typed alternating `C8` below, with its four old edges present and its
four new seams residence/common-cap legal.  The remaining source datum is an
addressed halo/return certificate; signed target equality cannot replace it.

## 1. When counter equality really gives an address bijection

Let `A` be a finite set of physical interval addresses.  In two phases let

\[
                 \rho_0,\rho_1:A\longrightarrow{\cal R}       \tag{1.1}
\]

record the protected row of an address.  For a graded compiler one takes
`R={(w,T)}`; for an ungraded compiler one takes `R={T}`.

### Theorem 1.1 (bucketwise occurrence transport)

There is a permutation `sigma` of `A` satisfying

\[
                    \rho_0(a)=\rho_1(\sigma(a))
                    \qquad(a\in A)                            \tag{1.2}
\]

if and only if

\[
       |\rho_0^{-1}(R)|=|\rho_1^{-1}(R)|
                    \qquad(R\in{\cal R}).                    \tag{1.3}
\]

When (1.3) holds, order the two fibres of every row by physical start and
then end address and pair equal ranks.  This is a canonical explicit
`sigma`.

If `M subseteq A` is any set of pairwise-distinct cells used by an old
matching, then `sigma(M)` is pairwise distinct and supplies the same target
rows in the new phase.  If pointwise source caps contain both phase words,
every transported interval also lies in the new cap.

#### Proof

Necessity follows because a permutation preserves every fibre cardinality.
Under (1.3), the order-preserving bijections between corresponding fibres
are disjoint and their union is a permutation of `A`, proving sufficiency.
Restriction of a permutation is injective.  The cap assertion follows by
unioning the pointwise caps over the transported interval.  \(\square\)

This theorem is the exact positive content of graded deck equality at the
occurrence level.  It does **not** say `rho_0(a)=rho_1(a)` at each address.
If a protected set `F subseteq A` must remain invariant, a transport with
`sigma(F)=F` exists if and only if (1.3) holds separately on `F` and
`A-F`.  If every address of `F` must be fixed pointwise, the additional
condition is

\[
                         \rho_0(a)=\rho_1(a)\quad(a\in F).    \tag{1.4}
\]

Thus the common-cut screened identity supplies a literal transport on the
whole mobile interval bank.  A matching-closed **background** needs the
separate restricted conditions above; this is exactly why unlabelled deck
equality alone was insufficient in the earlier notes.

The lightweight replay in Section 6 additionally finds, for `2<=d<=6`, a
perfect same-address common basis on all distinct graded rows of the
canonical screened plateau word.  This finite fact is useful but is not
promoted to an all-`d` theorem.

## 2. The coatom rail's exact lower discrepancy

Use the notation of
`MATH_THEOREM_THREAD_D_C8_ALIGNED_SINGLECUT_COATOM_LINK_20260801.md`.
Let `D` have size `r+2` and put

\[
 p=f_{d+1},\qquad q=f_0,                               \tag{2.1}
\]

while `x` and `y` are the second omissions of the first and last coatom
owners.  In the displayed rail they are

\[
 (x,y)=(f_2,f_1)\quad(d=2,3),\qquad
 (x,y)=(f_2,f_{d-1})\quad(d\ge4).                     \tag{2.2}
\]

The six labels `a_1,a_3,p,x,q,y` are pairwise distinct.  Define

\[
\begin{array}{ll}
 L_+=D-\{a_3,p,x\},&L_-=D-\{a_1,p,x\},\\
 R_+=D-\{a_1,q,y\},&R_-=D-\{a_3,q,y\}.              \tag{2.3}
\end{array}
\]

The minus rail contributes `L_-+R_-` at its two exterior lower edges and
the plus rail contributes `L_++R_+`.  Its upper boundary counter is already
phase independent.

## 3. A zero-count phase-dependent `C8` sidecar

Put

\[
       I_L=D-\{a_1,p,q\},\qquad I_R=D-\{a_3,x,y\}.    \tag{3.1}
\]

Define eight rank-`r` owners, cyclically ordered, by

\[
\begin{array}{llll}
 V_0=D-\{p,x\},&V_1=D-\{a_1,p\},&
 V_2=D-\{p,q\},&V_3=D-\{a_1,q\},\\
 V_4=D-\{q,y\},&V_5=D-\{a_3,y\},&
 V_6=D-\{x,y\},&V_7=D-\{a_3,x\}.                    \tag{3.2}
\end{array}
\]

Let

\[
 E_0=V_7V_0, E_1=V_0V_1,ldots,E_7=V_6V_7.          \tag{3.3}
\]

### Theorem 3.1 (upper-neutral lower-discrepancy circuit)

The `V_i` are distinct and (3.3) is an alternating `C8` in `J(*,r)`.  Its
lower colours in cyclic order are

\[
       L_+,L_-,I_L,I_L,R_+,R_-,I_R,I_R.              \tag{3.4}
\]

Its upper colours in cyclic order are

\[
 D-x,D-p,D-p,D-q,D-q,D-y,D-y,D-x.                    \tag{3.5}
\]

Consequently, selecting the even edges in the minus phase and the odd edges
in the plus phase has signed lower action

\[
 (L_++I_L+R_++I_R)-(L_-+I_L+R_-+I_R)
                  =L_++R_+-L_--R_-                  \tag{3.6}
\]

and zero signed upper action.  Added to the common coatom rail, both complete
lower and upper `q1` counters agree phase by phase.  The switch preserves
owner degrees and uses no new owner occurrence.

#### Proof

Consecutive omitted pairs in (3.2) share exactly one coordinate, so every
edge is Johnson.  Direct intersection gives (3.4), and direct union gives
(3.5).  Pairing even and odd entries proves (3.6) and upper equality.  The
six distinguished labels are different, so the eight omitted pairs, hence
the eight owners, are different.  Alternating a cycle preserves degree at
every vertex.  \(\square\)

This is a genuine exact sidecar, but its phrase “zero length” has a necessary
physical scope.  It is zero-count when the four even edges are already four
transition slots of the owner factor and the four odd edges reuse those
slots after segment reconnection.  A literal OR-word installation still
must certify the four new seams.  In the orientation of (3.2), those seams
exchange respectively

\[
        a_1\leftrightarrow x,quad a_1\leftrightarrow p,quad
        a_3\leftrightarrow q,quad a_3\leftrightarrow y.      \tag{3.7}
\]

Their prefix/suffix residence ages, source inverses and common caps are not
implied by the set calculation.  Topology is preserved as a 2-factor but a
chosen component can split or merge.

### Corollary 3.2 (literal q1 occurrence return)

Label the two rail boundary-edge addresses by `r_L,r_R`, and label the
sidecar edge addresses by `e_i`.  On the combined rail plus sidecar bank,
the lower-q1 address permutation can be chosen as

\[
\begin{array}{c|cccccc}
\text{minus address}&r_L&r_R&e_0&e_4&e_2&e_6\\ \hline
\text{plus address}&e_1&e_5&r_L&r_R&e_3&e_7,
\end{array}                                                \tag{3.8}
\]

with target rows respectively

\[
                 L_-,R_-,L_+,R_+,I_L,I_R.              \tag{3.9}
\]

The upper sidecar addresses return by

\[
                 e_0\mapsto e_7,quad e_2\mapsto e_1,
                 \quad e_4\mapsto e_3,quad e_6\mapsto e_5, \tag{3.10}
\]

while the two already phase-common rail upper addresses may be fixed.
Thus, subject only to the physical existence of the eight declared edge
occurrences, the sidecar gives an explicit bijection rather than a signed
value identity.

#### Proof

Read the lower labels from (2.3) and (3.4), and the upper labels from (3.5).
Every address on either side of (3.8) and (3.10) occurs exactly once, so the
displayed maps are bijections.  \(\square\)

### Proposition 3.3 (minimality of the sidecar support)

No nontrivial alternating `C4` can realize (3.6).  Hence any single
degree-preserving circuit which cancels the rail discrepancy uses at least
six edges; under exact upper-counter preservation and the displayed four
distinct prescribed colours, the construction (3.2)--(3.6) gives the first
uniform closed solution, of length eight.

#### Proof

At two consecutive edges of any owner circuit, the two lower colours are
both codimension-one subsets of the shared rank-`r` owner.  They are
therefore equal or Johnson adjacent.  In an alternating `C4`, the prescribed
sign pattern would have to pass directly from `L_-` to `R_+` and from
`R_-` to `L_+` after cyclic relabelling.  But

\[
 |L_-\triangle R_+|=|R_-\triangle L_+|=4,             \tag{3.11}
\]

because the filler omission pairs `{p,x}` and `{q,y}` are disjoint.  Thus
neither transition can occur at one shared owner.  This rules out `C4`.
The repeated intermediate rows in (3.4) are the two neutral relay pairs
which repair exactly those two gaps.  \(\square\)

The proposition does not classify every possible `C6`; the rigorous claim
needed here is the `C4` no-go and the explicit `C8` positive construction.

## 4. Why the basis-changing host does not combine with the common cut

Let `S_0,S_1` be the authenticated aligned folded source words, `G_0,G_1`
the canonical plateau two-ray words, and `Q_0,Q_1` the owner-legal words of
`MATH_THEOREM_K_FOLDED_C8_BASIS_CHANGING_RAY_SOCKET_AND_EXTERIOR_RETURN_GATE_20260801.md`
at its optimal end gap.  The common cut and common active screen give

\[
        D_{\rm gr}(S_0G_1)=D_{\rm gr}(S_1G_0).        \tag{4.1}
\]

Replacing `G` by `Q` destroys (4.1).  Write

\[
 H_0=K+za_0a_1a_2+F[1,d],\qquad
 H_1=K+za_0a_2a_3+F[1,d].                             \tag{4.2}
\]

At the same common cut, the exact signed residue is

\[
\begin{aligned}
 \Delta={}&\sum_{w=2}^{d+1}\bigl[(w,H_1)-(w,H_0)\bigr]\\
 &+\sum_{w=2}^{d}\Bigl(
  (w,K+za_1+F[1,w-1])-(w,K+za_3+F[1,w-1])\\
 &\hspace{34mm}+(w,K+za_3+F[d-w+2,d])
             -(w,K+za_1+F[d-w+2,d])\Bigr).            \tag{4.3}
\end{aligned}
\]

All displayed rows are distinct and have coefficient one.  Therefore

\[
                           \|\Delta\|_1=6d-4.          \tag{4.4}
\]

#### Proof

Subtract (4.1).  The fresh marker and neutral separator of `Q` contribute
only phase-common rows.  The first line of (4.3) is the changed full folded
row at widths `2,...,d+1`; the next two lines are the shifted prefix and
suffix rays at widths `2,...,d`.  This is the interval classification of the
basis-changing packet specialized to the common cut.  The common screen
contains both active labels and hence adds no further phase-sensitive row.
Disjoint active labels and proper prefix/suffix filler intervals prove
distinctness.  Counting gives `2d+4(d-1)=6d-4`.  \(\square\)

### Corollary 4.2 (direct composition obstruction)

There is no permutation of physical interval addresses which returns every
graded target row between `S_0Q_1` and `S_1Q_0`: their row counters differ by
(4.3).  In particular the canonical common-cut address transport cannot be
reused after the owner-legal substitution, even though `Q` has the correct
owner edge, ray support and pointwise common cap.

The replay verifies (4.3)--(4.4) for `2<=d<=6`, in both concatenation orders
and over every common cut.  Its minimum is always `6d-4`; the original
plateau word has minimum zero and an exact same-address common basis on the
same audited range.

## 5. Exact surviving splice condition

The coatom rail and the `C8` sidecar solve the local owner and both `q1`
counter rows.  They do not solve the source-address row.  The coatom rail
has `d+1` owner rows and maximal inverse length `2d+1`; it is scalar-neutral
only if its left and right `d`-letter halos are identified with an already
allocated ambient segment.  The direct aligned right-end identification is
already ruled out in the coatom-link theorem.

Thus an exact zero-charge lift now needs the following and no weaker
value-counter statement suffices.

1. Four old owner edges equal to `E_0,E_2,E_4,E_6`, with the four new seams
   `E_1,E_3,E_5,E_7` passing their occurrence-labelled residence and source
   cap tests.
2. An occurrence map for the `2d+1` coatom source rows whose first and last
   letters are `X_L,X_R` and whose two `d`-cell halos are recycled in the
   ambient prefix/suffix.  Recycling the common screen is legal only when an
   existing boundary cell literally contains the chosen screen and all
   owner/maximal-erosion constraints at that address remain exact.
3. On the mobile address bank, the bucket transport of Theorem 1.1.  On every
   frozen background bank, the restricted bucket equality (and pointwise
   equality when addresses themselves are frozen).
4. One common cap state in which the transported matching and the ray
   diagonal are disjoint and every selected interval reconstructs its target.

Alternatively, retaining the short owner-legal packet `Q` requires an
exterior return bank for every positive row of (4.3), with a matching into
the negative/released address bank in the same cap state.  Its unavoidable
local demand has `3d-2` rows per sign.  The common-cut cancellation alone
does not supply that matching.

## 6. Independent replay

The dependency-light audit

```text
scratch/audit_r_c8_ownerlegal_commoncut_address_and_sidecar_20260801.py
scratch/r_c8_ownerlegal_commoncut_address_and_sidecar_20260801.audit.json
```

checks `2<=d<=6` under a local-memory run:

* both block orders and every common cut;
* the exact `6d-4` minimum after the owner-legal substitution;
* zero graded residue for the original screened plateau word;
* a perfect common physical-address basis for every distinct graded and
  ungraded row of that original word; and
* all eight owner, lower-colour and upper-colour identities in Theorem 3.1.

Frozen hashes after the replay are recorded in the handoff.  The symbolic
proofs above, not extrapolation from the finite range, establish Theorems
1.1 and 3.1 and formula (4.3) for general `d`.
