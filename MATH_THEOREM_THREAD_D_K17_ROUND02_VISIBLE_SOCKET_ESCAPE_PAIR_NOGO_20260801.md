# The round02 visible-socket pair face is closed

Date: 2026-08-01  
Status: exact for unordered pairs of the twelve certified one-recut socket escapes

## 1. The bounded face

Let `V` be the twelve noncentral cut substitutions in
`round02.socket_escape_v2.tsv`.  Each member of `V` individually preserves
the complete zero-265 singleton ledger and exposes a non-`114930` seam at
one of the two dual-fan sockets.

This note considers exactly the face

\[
                 {\cal F}_2=\{\{u,v\}:u,v\in V, u\ne v\}.       \tag{1.1}
\]

There are 66 formal unordered pairs.  One pair chooses the two different
replacements `12065->12067` and `12065->12066` in the same base piece 2251,
so it is not a simultaneous cut assignment.  The remaining 65 are the
compatible face.

## 2. Literal joint replay

For every compatible pair, both substitutions were applied simultaneously
to the original round02 base-piece assignment.  The full occurrence-labelled
atlas was then reconstructed; the computation did not add the effects of two
single-child summaries.

**Theorem 2.1.** All 65 compatible pairs have

* zero lower-colour, outgoing-piece, incoming-piece,
  common-orientation, and rank-ten singleton failures;
* a genuine socket escape;
* pairwise different complete local socket-atlas signatures.

The relaxed atom count ranges from 228,706 to 228,886.  The numbers of
directed noncore socket incidences range from 0 to 18 at `s=115442` and from
0 to 28 at `t=115186`.  No pair creates the direct shared-`114930` seam.

The complete literal score takes 2.39 seconds and 19,660 KiB on one H100 CPU
core.  Its implementation and result are

* `scratch/threadD_k17_round02_dualfan_escape_pairs_20260801.cpp`, SHA-256
  `e6fd3f7cb423b51a1b01313ae49b987de881130c4dc1ffb7c4025101bef00d04`;
* `scratch/threadD_k17_round02_escape_pairs_20260801/pairs.tsv`, SHA-256
  `7b2edd1557f4fe94e6c88acdc362ffb18b88cd21f8bf6e03eb3699f5c89556b7`;
* its audit JSON, SHA-256
  `fe5fb127e9d405574f9e1b7da7f2cc7fcdb98794ce0a881e6497819099123b70`.

## 3. Exact q1 verdict and proof replay

For every one of the 65 clean pair banks, the exact orientation/seam/selected-
colour q1 formula was generated.  Its size ranges were

\[
  891538\le n_{var}\le892259,
  \qquad
  2416486\le n_{clause}\le2418469.                         \tag{3.1}
\]

All 65 formulas are UNSAT.  This is stronger than the requested
q1-plus-rank-ten verdict: conjoining the exact rank-ten survival rows to an
already UNSAT q1 formula remains UNSAT.  Independently, every CNF was solved
again with proof output and every DRAT proof was accepted by `drat-trim`.
The backward proof cores use 20--187 original clauses and 10--86 lemmas.
The sequential one-core proof regeneration and verification took about
193 seconds.

The exact manifests are

* q1 bank/CNF/result summary SHA-256
  `b2cdcece539162e9a0eee4ad4ebcdfc0597cc075e0b8732674511753add8a39b`;
* regenerated proof manifest SHA-256
  `006c2c09177248228cf40a20d78472ee28abcc581c95308050546f3db6a1f3f3`;
* independent verification driver SHA-256
  `26108028a0af26825f1d8abb7da1f30b5f272cad651685a826e4e068cfc088eb`.

The proof manifest records all 65 CNF and proof hashes, and every row has
`result=UNSATISFIABLE` and `drat_verified=1`.  A local manifest cross-check
also confirms that its 65 CNF hashes equal the hashes in the independent
q1 portfolio summary.

## 4. Exact scope and next face

Therefore no compatible pair of **two individually visible, zero-265-clean
socket escapes** completes q1 on the fixed round02 one-split-per-base face.

This is not a general Hamming-two theorem.  In particular it does not cover

1. two recuts neither of which exposes a socket in its single child but which
   jointly activate a seam or its selected lower colour;
2. a visible escape paired with a neutral rerouter outside `V`;
3. compensation of an individually dirty central or noncentral recut;
4. raw latent endpoint times other-recut-colour activations;
5. added cuts, alternative base decompositions, or compound circuits.

The central `9933->9932` recut is locally inadmissible by itself, whereas
`9924->9923` is the sole clean central recut.  A complete next anchor must
nevertheless retain all nine central alternatives as guarded columns,
because a second recut may compensate a local zero.  The exact next search is
thus the synergistic/latent Hamming-two face, not another scan of pairs from
`V`.

