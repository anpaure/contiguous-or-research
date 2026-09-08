# The 108 forced nonflat `K17` blocks share one owner-phase run

Date: 2026-07-31  
Status: exact finite theorem and literal bit-trace replay; complementary
facet-rail embedding and the common cap remain open

## 0. Result

The local owner/cofacet zipper theorem advances 108 disjoint A-shore blocks
one derivative row.  Installed independently, those blocks appeared to cost
108 phase boundaries against one available linear opening, leaving a scalar
debt of 107.

That debt is **not** an invariant.  There is an orientation and ordering of
all 108 owner blocks such that their concatenation has no strictly internal
positive coordinate run shorter than three.  Consequently its derivative
has no strictly internal positive run shorter than four.  The whole selected
bank may therefore occupy one owner-phase run, whose single phase component
uses exactly the one available linear opening.

The authenticated witness has:

```text
selected blocks                         108
compatible directed oriented joins    2178
SAT cycle-cut rounds                     58
concatenated owner tokens              1958
internal D2 runs below 3                   0
internal D3 runs below 4                   0
owner-phase components                     1
scalar phase-component debt                0
```

This closes only the scalar phase-sharing row.  It does not yet embed the
complementary lower-facet pieces into the other phase, restitute every
displaced palette value, or construct one depth-zero common cap.

## 1. Exact join criterion

Let `P` and `Q` be two oriented owner blocks.  Every strictly internal
positive run in either block already has length at least three.  Therefore
`P Q` creates a new short run only at the join.

For coordinate `x`, let `s_x(P)` be the positive suffix length of `P` and
`p_x(Q)` the positive prefix length of `Q`, with value zero when the
corresponding endpoint is zero.  The join is legal exactly when, for every
`x`,

* if both endpoints are positive, `s_x(P)+p_x(Q) >= 3`;
* if only the left endpoint is positive, `s_x(P) >= 3`; and
* if only the right endpoint is positive, `p_x(Q) >= 3`.

This condition is necessary and sufficient because no other run boundary
changes.  It is also invariant under reversing the whole concatenation.

## 2. Oriented Hamilton-path certificate

Make a directed graph with two vertices `(M,+)` and `(M,-)` for every one
of the 108 selected macros.  Put an arc from one oriented macro to another
exactly when the criterion in Section 1 holds.

The certificate chooses one orientation of every macro and 107 compatible
arcs forming one directed Hamilton path.  The SAT encoding uses:

1. exactly one orientation per macro;
2. exactly one global start and one global end;
3. exactly one predecessor except at the start;
4. exactly one successor except at the end; and
5. lazy clauses excluding every directed cycle in a provisional path
   cover.

After 58 cycle-cut rounds the model is a single 108-vertex path.  The
verifier reconstructs all 1958 literal owner masks from the frozen parent
and flow artifacts, applies the recorded orientations, and checks every bit
run directly.

## 3. Derivative residence

Let `R` be the concatenated owner word.  For one coordinate, a strictly
internal positive run of length `ell` in `R` becomes a positive run of
length `ell+1` in `DR`, because adjacent OR expands it by one edge on each
side overall.  Since every such run in `R` has length at least three, every
strictly internal run in `DR` has length at least four.  The literal replay
independently confirms both rows.

Thus the selected owner bank satisfies the local depth-two/depth-three
residence thresholds as one phase component, not as 108 separately opened
modules.

## 4. Exact remaining gate

The result changes the global realization problem substantially but does
not finish it.  A complete optimal-length schedule must now construct one
mixed depth-two word with:

1. this owner-phase path placed at a linear boundary;
2. all complementary rank-eight facet pieces rethreaded into the opposite
   phase with one compatible interface;
3. every rank-nine owner and displaced lower/upper palette value witnessed;
4. no new short run at the phase interface; and
5. one common depth-zero cap realizing all remaining lower targets.

The correct next object is therefore a **two-bank socket rethread**, not a
payment of 107 independent positions.

## 5. Reproducibility

```text
python3 scratch/search_k17_nonflat_phase_path_20260731.py
```

Artifacts:

```text
scratch/search_k17_nonflat_phase_path_20260731.py
SHA-256 be3ac283144c302f913c75b7d2adb0c9b8ec8bc7b667d603cf370a8007120b0b

scratch/k17_nonflat_phase_path_20260731.json
SHA-256 68f203728da4c476262ad07eaac8ed0be65f8435ac598bce29e7ad275031f853
payload SHA-256 e72a300619766803476163b2972fbf946850c335081691abf40951c276738546
```

Authenticated inputs are recorded by SHA-256 inside the JSON.  No `K17`
word, improved numerical upper bound, all-`k` construction, or common-cap
certificate is claimed.
