# Independent audit of the sharp pivot aperture, literal source block, and clipped residence collar

Date: 2026-08-01  
Lane: independent audit of the proposed noncanonical monotone-pivot host  
Status: **GO with two scope corrections and one false rigidity sentence removed.**

## 0. Verdict

The main construction is correct.

* The aperture inequality
  \[
       |X|\le r-h
  \]
  follows from a literal deletion count and is sharp.
* The displayed `2h`-letter source, after inserting `X`, gives the claimed
  `h+1` distinct rank-`r` owners, a simple Johnson **geodesic**, pairwise
  distinct lower and upper immediate colours, and literal preservation of
  every old interval OR.
* Inside the strict-lower band the only new values are the singleton and the
  two displayed nested rays.  Subject to the hypotheses of the existing
  flat monotone-pivot compiler theorem, these rays give zero residual lower
  deficiency.
* The `3h+1`-owner collar is rank-`r`, simple, Johnson, and doubly q1-rainbow.
  Every central `lambda_j` and `rho_j` has one run of length exactly `h+1`.
  The ground-set count `k>=r+3h` is exact for this labelled realization.
* After specializing to `k=2m-1,r=m`, an incidence-vertex-disjoint bank of
  `H` such paths has `6Hh` protected incidence edges, so the small
  protected-factor theorem applies under `6Hh<=m-2` on the odd
  middle-level host `ML_m`.

Three qualifications are load-bearing.

1. The claimed equality-case rigidity is too strong: equality in the
   aperture bound need not make the owner path geodesic.  Deleted labels may
   re-enter later.  The explicit construction is geodesic because its `L`
   and `R` banks are disjoint, but this does not classify every equality
   case.
2. “Exact local compiler closure” is conditional on the hypotheses already
   present in the monotone-pivot theorem: a flat surrounding derivative, a
   reference strict-lower matching whose old target bank omits the new task
   `X`, occurrence-labelled release of the `2h-2` ray targets, and one
   simultaneous cap-legal source word.  The local block alone does not
   construct the ambient matching or global cap.
3. The far-left and far-right collar coordinates are clipped boundary
   flags, not resident internal runs.  They must be extended or discharged
   by the exterior host.  The small protected-factor theorem preserves the
   collar path but does not supply those exterior residence continuations,
   upper surjectivity, bounded component count, or a common cap.

No enumeration is needed for these conclusions.

## 1. Aperture inequality

Insert `X` at a cut with at least `h` old letters on each side, and number
the `h+1` new length-`h+1` windows through `X` by `M_0,...,M_h` from left to
right.

For a coordinate `z notin X`, occurrences to the left of the cut contribute
an initial segment of the window indices, while occurrences to the right
contribute a final segment.  Therefore

\[
       \{j:z\in M_j\}
\]

is a prefix union a suffix and has at most one `1 -> 0` transition.  At each
of the `h` transitions `M_(j-1) -> M_j`, distinct equicardinal sets force at
least one deletion.  A coordinate cannot account for two such deletions,
no member of `X` can be deleted, and every deleted coordinate starts in
`M_0\X`.  Hence

\[
       h\le |M_0\setminus X|=r-|X|.
\]

This proves the necessary bound exactly as claimed.

### 1.1 Correction to the equality statement

At equality there is exactly one deletion and, by rank conservation, one
insertion at every step.  Thus one may write

\[
 M_j=X\cup\{\rho_1,\ldots,\rho_j\}
        \cup\{\lambda_{j+1},\ldots,\lambda_h\},
\]

with the understanding that a deleted label may reappear later.  This is an
ordered one-swap normal form, but it is not automatically a geodesic.

If `L` is the deletion bank and `R` the insertion bank, then

\[
                         d_J(M_0,M_h)=h-|L\cap R|.       \tag{1.1a}
\]

The banks are separately simple because every coordinate trace has at most
one deletion and at most one insertion.  Their intersection consists
exactly of the labels which are deleted and later reinserted.  Hence an
equality-case path is geodesic if and only if `L cap R` is empty.

For example, with `h=2`, `r=3`, and distinct `x,a,b,c`, take the literal old
word

\[
       \{a\},\ \{x,b\}\mid\{x,c\},\ \{a\}
\]

and insert `X={x}`.  The three owners are

\[
       \{x,a,b\},\quad \{x,b,c\},\quad \{x,c,a\}.
\]

They are distinct rank-three Johnson neighbours, satisfy the monotone
condition `X subseteq {x,b} union {x,c}`, and attain `|X|=r-h`.  But the
first and last owners are adjacent, so the two-step path is not geodesic.
The label `a` is deleted and then reinserted.  Thus the universal rigidity
claim needs the extra condition that the deletion and insertion banks are
disjoint (equivalently, endpoint Johnson distance `h`).

## 2. The explicit source block

Let `|Q|=r-h`, `X subseteq Q`, and take disjoint ordered banks

\[
 L=(\lambda_1,\ldots,\lambda_h),\qquad
 R=(\rho_1,\ldots,\rho_h)
\]

outside `Q`.  The old word is

\[
 \{\lambda_1\},\ldots,\{\lambda_{h-1}\},Q+\lambda_h
 \mid
 Q+\rho_1,\{\rho_2\},\ldots,\{\rho_h\}.
\]

After inserting `X`, the windows through it are exactly

\[
 M_j=Q\cup\{\rho_1,\ldots,\rho_j\}
       \cup\{\lambda_{j+1},\ldots,\lambda_h\},
       \qquad 0\le j\le h.
\]

Disjointness makes every `M_j` have rank `r`, and

\[
 M_{j+1}=M_j-\lambda_{j+1}+\rho_{j+1}.
\]

The endpoint difference has size `h`, so this particular path really is a
Johnson geodesic.  Its immediate colours are

\[
 I_j=Q\cup\rho[1,j]\cup\lambda[j+2,h],
 \qquad
 U_j=Q\cup\rho[1,j+1]\cup\lambda[j+1,h].
\]

Their changing prefix/suffix split proves pairwise distinctness within each
palette.  The construction uses `|Q|+2h=r+h` labels, proving sharp
realizability whenever `k>=r+h`.

## 3. Literal deck transparency

Every old interval on one side of the cut transports by an index shift.
Every old interval crossing the cut contains both adjacent letters
`Q+lambda_h` and `Q+rho_1`, so its old union contains `Q`, hence contains
`X`.  Adding the inserted letter therefore changes no such union.  Thus

\[
       Deck(A_old)\subseteq Deck(A_new)
\]

with a literal witness injection, at every width and in every exterior
context.

This is OR preservation, not width preservation.  A noncrossing interval
keeps its width, while a crossing interval contains the inserted source
position and its width rises from `w` to `w+1`.  Thus arbitrary-width target
coverage transports, but a width deadline must use the separate band
calculation below.

The old crossing length-`h+1` windows are exactly

\[
       U_j=M_j\cup M_{j+1},\qquad 0\le j<h,
\]

as claimed.

## 4. Strict-lower band and compiler scope

In the interval band of source length at most `h`, insertion has exactly the
new cells

\[
 X,qquad
 P_i=Q\cup\{\lambda_{h-i+1},\ldots,\lambda_h\},qquad
 S_i=Q\cup\{\rho_1,\ldots,\rho_i\},quad 1\le i<h.
\]

Their ranks are `|X|` and `r-h+i<r`.  They are pairwise distinct, and both
non-singleton banks are strict nested chains.  The next one-sided cells are
`M_0` and `M_h`, already rank `r`; any longer one-sided interval contains
one of these.  Hence these are indeed all genuinely new strict-lower cells,
not merely all new cells of a fixed width.

The existing flat monotone-pivot theorem now applies exactly as follows.
The `h-1` old band cells lost under transport have the same values as the
new central owner windows and therefore have rank `r`.  A reference matching
of strict-lower targets uses none of them.  Release the old matching edges
of the occurrence-labelled targets `P_i,S_i`, transport every other edge,
and place `P_i,S_i,X` on the new cells.  This gives zero residual deficiency
provided:

* `X` is the new task and is outside the old target bank;
* every `P_i,S_i` is an old target with an edge in the reference matching;
* the entire surrounding final derivative is flat rank `r`; and
* the displayed source, together with all exterior rows, passes the one
  simultaneous common-cap/maximal-word test.

Thus the proposal closes the formerly missing **local pivot-rich source
row**, but it does not by itself construct the ambient old compiler or a
global protected host.

## 5. The clipped collar

Choose `q in Q`, fresh `q^-,q^+`, and disjoint fresh banks
`D^-=(d^-_1,...,d^-_(h-1))`, `D^+=(d^+_1,...,d^+_(h-1))`.  Put

\[
 Q^-=(Q-q)+q^-,\qquad Q^+=(Q-q)+q^+.
\]

The proposed owners are

\[
 L_t=Q^-\cup\lambda[1,t+1]\cup D^-[t+1,h-1],
\]

\[
 R_t=Q^+\cup\rho[t+1,h]\cup D^+[1,t],
 \qquad 0\le t<h,
\]

with `M_0,...,M_h` between the two banks.

### 5.1 Rank, simplicity, and Johnson adjacency

Both `L_t` and `R_t` have rank `r`.  Consecutive left owners exchange
`d^-_(t+1)` for `lambda_(t+2)`; `L_(h-1)->M_0` exchanges `q^-` for `q`.
The central transitions exchange `lambda_(j+1)` for `rho_(j+1)`;
`M_h->R_0` exchanges `q` for `q^+`; consecutive right owners exchange
`rho_(t+1)` for `d^+_(t+1)`.  The special labels `q^-,q,q^+` separate the
three blocks, so all `3h+1` owners are distinct.

### 5.2 Immediate palettes

The lower intersections are, respectively,

\[
 Q^-\cup\lambda[1,t+1]\cup D^-[t+2,h-1],
\]

the left boundary `(Q-q) union lambda[1,h]`, the central `I_j`, the right
boundary `(Q-q) union rho[1,h]`, and

\[
 Q^+\cup\rho[t+2,h]\cup D^+[1,t].
\]

The upper unions have the analogous extra exchanged label.  Within a block,
the moving prefix/suffix index distinguishes them.  For upper colours, the
presence pattern of `q^-,q,q^+` separates all five classes.  For lower
colours, both seam intersections omit all three special labels, so that
signature alone does not separate them; they are instead `(Q-q) union L`
and `(Q-q) union R`, distinct because the two `h`-banks are disjoint.  All
other lower cross-class collisions are excluded by the special-label
signature.  Hence both local q1 palettes are collision-free.  Across
several collars this conclusion requires the stated resource-disjointness;
it is not a consequence of the one-collar formulas.

### 5.3 Residence

For `1<=j<=h`, `lambda_j` occurs in `h-j+1` terminal left-collar owners and
the first `j` central owners.  Its run is consecutive and has length `h+1`.
Similarly, `rho_j` occurs in `h-j+1` terminal central owners and the first
`j` right-collar owners, again one run of length `h+1`.  The coordinate `q`
has the central run `M_0,...,M_h`, also of length `h+1`; every member of
`Q-q` persists throughout.

By contrast, `q^-` and every `d^-_s` form prefixes touching the far-left
endpoint, and `q^+` and every `d^+_s` form suffixes touching the far-right
endpoint.  Their run lengths can be below `h+1`.  Therefore (and consistently
with the proposal's wording) this is a **clipped** residence collar.  It is
resident only after the ambient host supplies legal exterior continuation
or treats these flags as genuine linear boundaries.

The exact local halo demand is as follows.  For `1<=s<h`, the clipped run
lengths are

\[
 \begin{array}{c|c}
 q^-&h\\
 d^-_s&s\\
 q^+&h\\
 d^+_s&h-s.
 \end{array}                                             \tag{5.1}
\]

Let `a_L(x)` (respectively `a_R(x)`) denote the number of consecutive
exterior owners immediately before (respectively after) the displayed path
which contain `x`.  An internal ambient splice with residence floor `h+1`
then needs

\[
 a_L(q^-)\ge1,qquad a_L(d^-_s)\ge h+1-s,               \tag{5.2}
\]

consecutive owners on the left, and

\[
 a_R(q^+)\ge1,qquad a_R(d^+_s)\ge s+1                 \tag{5.3}
\]

consecutive owners on the right.  These inequalities repair only the
displayed boundary runs; the ambient completion must also avoid creating a
separate short run of the same coordinate elsewhere.

The labels used are `Q`, `L`, `R`, the two replacement labels, and
`2(h-1)` flag labels, totaling

\[
       (r-h)+2h+2+2(h-1)=r+3h.
\]

Thus `k>=r+3h` is exactly sufficient for this labelled collar.

## 6. Fixed-`H` factor planting

Specialize now to `ML_m` on `[2m-1]` and set `r=m`.

The collared owner path has `3h` Johnson transitions.  Its lift to the
middle-level containment graph has `6h` incidence edges.  If `H` copies are
resource-disjoint in owners and lower q1 colours, their union is 2-bounded
and contains `6Hh` edges.  The small protected-factor theorem therefore
embeds the bank in a spanning two-factor whenever

\[
       6Hh\le m-2.
\]

For fixed `H` and `h=Theta(sqrt(m))`, this holds in all sufficiently large
odd middle-level hosts `ML_m` on `[2m-1]`.

This is conditional on first specifying incidence-vertex-disjoint copies;
the local packet theorem does not itself pack such a bank.  Coordinate-set
disjointness is neither required nor generally possible, since one collar
already uses `m+3h` of the `2m-1` coordinates.  It also
does not directly cover the unbalanced even-dimensional incidence graph;
an even construction must identify the odd host/subsystem or invoke its
separate Pascal lift.  Finally, the factor completion is arbitrary: it need
not be upper-surjective, have `O(H)` components, continue the clipped flags,
preserve global residence/all-width witnesses, or admit the final common
cap.

## 7. Correct proof boundary

The new result genuinely removes the local noncanonical pivot-rich-chain
existence line.  After the corrections above, the remaining owner-layer
target is precisely a protected rooted Catalan-connector theorem containing
this fixed geodesic bank, plus exterior residence continuation and the
global compiler/cap rows.  No local rank, q1, arbitrary-width OR, or
strict-lower ray obstruction remains in the displayed packet itself.
