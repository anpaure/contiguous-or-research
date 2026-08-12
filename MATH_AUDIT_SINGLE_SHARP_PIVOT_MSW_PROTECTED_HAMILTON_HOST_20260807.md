# Independent audit of the single-sharp-pivot MSW protected Hamilton host

**Date:** 2026-08-07  
**Audited file:**
`MATH_THEOREM_SINGLE_SHARP_PIVOT_MSW_PROTECTED_HAMILTON_HOST_20260807.md`  
**Method:** line-by-line set calculation plus primary-source support audit  
**Verdict:** **PASS.**  No substantive correction is required.  The theorem
is an unconditional Hamilton-host theorem for one prescribed shortest pivot
geodesic, with exactly the global exclusions stated in its Section 5.

## 1. Parameters and the three-piece buffer

The central path has normal form

\[
 T_j=C\cup\{b_1,\ldots,b_j\}
       \cup\{a_{j+1},\ldots,a_h\},
 \qquad |C|=m+1-h.
\]

The hypothesis \(3h\le m-1\) gives both required resources:

\[
 |C|-2h=m+1-3h\ge2,
\]

so the disjoint banks \(C^-,C^+\subset C\) exist, and

\[
 |[2m+1]\setminus(C\cup A\cup B)|=m-h\ge2h+1,
\]

so disjoint \(D^-,D^+\) and \(z\) exist.

The buffered owner sequence exchanges, in order,

\[
 D^-\to C^-,\qquad A\to B,\qquad C^+\to D^+.
\]

Its \(3h\) leaving labels and \(3h\) entering labels are separately
distinct and mutually disjoint.  Hence it is a shortest Johnson geodesic,
not merely a simple walk.  Every owner avoids \(z\).

**Audit result:** PASS.

## 2. Geodesic-extension lemma

Let

\[
 Y_j=Y_0-\{p_1,\ldots,p_j\}+\{q_1,\ldots,q_j\}
\]

be a shortest rank-\((m+1)\) geodesic in a \(2m\)-set, with
\(t\le m-1\).  Its common core has size \(m+1-t\ge2\), so distinct
\(c_-,c_+\) may be chosen.  The proposed rank-\(m\) sets satisfy

\[
 X_0=Y_0-c_-,\qquad
 X_{j+1}=Y_j-p_{j+1}\ (0\le j<t),\qquad
 X_{t+1}=Y_t-c_+.
\]

Direct subtraction shows that the successive exchanges are

\[
 p_1\to c_-,\quad p_{j+1}\to q_j\ (1\le j<t),
 \quad c_+\to q_t.
\]

All leaving labels lie in \(X_0\), all entering labels lie outside
\(X_0\), and the two banks are disjoint.  Therefore the remaining
\(m-t-1\) elements of \(X_0\) may be bijected with the remaining
\(m-t-1\) elements of its complement, extending the path to exactly
\(m\) exchanges and endpoint \(\Omega\setminus X_0\).

For every protected index,

\[
 X_j\cup X_{j+1}=Y_j,
\]

and, equivalently for adjacent protected owners,

\[
 X_{j+1}=Y_j\cap Y_{j+1}.
\]

Thus the desired owner path is literally the union trace of the completed
rank-\(m\) complementary geodesic.  There is no missing endpoint or
off-by-one exchange: \(Y_0,\ldots,Y_t\) use
\(X_0,\ldots,X_{t+1}\).

**Audit result:** PASS.

## 3. Coordinate-conjugacy check

Every complementary rank-\(m\) geodesic has an ordered leaving bank
\((\lambda_1,\ldots,\lambda_m)\) and an ordered entering bank
\((\rho_1,\ldots,\rho_m)\).  A coordinate permutation taking the two
ordered banks of one such path to those of another maps the complete
incidence path, including every intervening union, to the second path.

Consequently it is sufficient that the MSW/MNW Hamilton cycle retain one
canonical complementary path.  Applying the same coordinate permutation
to the entire Hamilton cycle, while fixing \(z\), retains the prescribed
completed path from Section 2.

**Audit result:** PASS.

## 4. Primary-source MSW/MNW support check

The relevant source is T. Mütze, J. Nummenpalo and B. Walczak,
*Sparse Kneser graphs are Hamiltonian*, J. London Math. Soc. 103 (2021),
1253--1275, DOI 10.1112/jlms.12406; see especially its Section 6.

The support statement used here is stronger than bare middle-levels
Hamiltonicity but is present in that proof:

1. the starting factor consists of the canonical MSW paths \(P(x)\)
   closed by the complement edges \(\{x,\bar x\}\);
2. every flipping cycle lies in the bipartite incidence graph, so symmetric
   difference never removes a complement closure edge;
3. after removing those retained closure edges, the paper combines the
   rethreaded path forest in one half with the unchanged canonical MSW
   forest in the other half; and
4. full complementation swaps the halves and makes the unchanged canonical
   forest the \(z\)-free half.

Thus the endpoint-augmented theorem cited by the audited note genuinely
produces a middle-levels Hamilton cycle retaining the complete chosen
canonical geodesic.  It is not an inference from ordinary Hamiltonicity.

The published odd-graph theorem applies for parameter at least three; in
the present nontrivial range \(h\ge1\) and \(3h\le m-1\), one has
\(m\ge4\), so there is no small-parameter gap.

**Audit result:** PASS.

## 5. Residence audit

On the protected owner interval:

* \(a_i\) is present throughout all \(h+1\) left-buffer owners and until
  its central deletion;
* \(b_i\) is present from its central insertion through all \(h+1\)
  right-buffer owners;
* every element of \(C^-\) persists to the right endpoint after entering;
* every element of \(C^+\) is present from the left endpoint until leaving;
* every element of \(C^0\) is constant; and
* runs of \(D^-\) and \(D^+\) meet the left and right endpoints,
  respectively.

Therefore every central active coordinate has a positive run of at least
\(h+1\) owners, and every other nonconstant run shorter than \(h+1\) is
an endpoint-clipped flag.  This is exactly local positive residence.  It
does not assert a residence floor for the unprotected Hamilton-cycle
complement or for the eventual cyclic continuation of the two flags.

**Audit result:** PASS with the theorem's stated local scope.

## 6. Immediate-palette audit

Write a shortest geodesic as

\[
 S_j=K\cup\{q_1,\ldots,q_j\}
          \cup\{p_{j+1},\ldots,p_t\}.
\]

Then the immediate lower and upper colours at transition \(j\) are

\[
 S_{j-1}\cap S_j
 =K\cup\{q_1,\ldots,q_{j-1}\}
      \cup\{p_{j+1},\ldots,p_t\},
\]

and

\[
 S_{j-1}\cup S_j
 =K\cup\{q_1,\ldots,q_j\}
      \cup\{p_j,\ldots,p_t\}.
\]

The ordered prefix/suffix signature determines \(j\), so both families
are pairwise distinct.  The lower colours are the literal intervening
rank-\(m\) vertices of the retained incidence path.  The upper colours are
distinct set values; they are not vertices of the middle-levels graph and
the theorem does not claim otherwise.

**Audit result:** PASS.

## 7. Exact scope boundary

The theorem closes precisely this statement:

\[
 \boxed{\text{one prescribed sharp-pivot owner geodesic has a locally
 resident, doubly-rainbow incidence lift inside a Hamilton cycle}.}
\]

It does **not** prove:

1. simultaneous retention of several independently prescribed pivot
   paths;
2. global depth-\(h\) coordinate residence;
3. the arbitrary-width upper OR deck;
4. a depth-\(h\) literal antecedent for the entire Hamilton owner cycle;
5. transport or existence of the global lower compiler/common cap; or
6. \(\nu(k)\le B(k)+1\) without those additional rows.

These exclusions agree with the audited theorem's status and Section 5.

## 8. Nonmathematical corrections

The source contains a few lost TeX backslashes in prose-rendered displays
(`ldots`, `quad`, `Updownarrow`-style lineage inherited from adjacent
notes).  They do not alter any definition or inference, but may be repaired
before publication.

**Final verdict:** PASS; no mathematical correction required.

