# Audit of coordinatewise Catalan run pressure and the exact connector transducer

Date: 2026-07-31  
Verdict: **PASS after the multi-seam and marked-cut scope was made
explicit**; exact characterization, not an all-\(m\) existence theorem

Audited file:

~~~text
MATH_THEOREM_R_CATALAN_COORDINATE_RUN_PRESSURE_AND_EXACT_CONNECTOR_TRANSDUCER_20260731.md
~~~

## 1. Coordinate identities

For a fixed coordinate \(x\), the induced source forest has

\[
 {2m-1\choose m-1}-{2m-1\choose m-2}
 ={1\over m+1}{2m\choose m}=\operatorname {Cat}_m
\]

components.  A selected Johnson seam decreases this count precisely when
its intersection colour contains \(x\).  Hence

\[
 r_x=K-s_x,\qquad \sum_xs_x=(m-1)K
\]

is exact for a cyclic \(K\)-seam joining.

The identity

\[
 (\ell-h)_+-(h-\ell)_+=\ell-h
\]

gives

\[
 E_x^{(h)}-D_x^{(h)}
 ={m+1\over2}K-h(K-s_x)
\]

with no asymptotic loss.  Its sum is
\((m+1)K(m-h)\).  The cyclic quota
\(s_x\ge K-\lfloor n_x/h\rfloor\) follows exactly.

For a Hamilton path, the endpoint correction is also valid.  If both word
endpoints contain \(x\), their positive boundary arms are distinct because
the spanning path contains vertices which omit \(x\).  Removing the
\(b_x\) exempt arms gives

\[
 n_x\ge h(K-s_x-b_x)+b_x,
\]

and therefore the displayed floor formula.  These are necessary scalar
conditions only.

## 2. Matching and collar rows

After indexing the upper colours by the source perfect matching, any other
perfect diamond matching is a permutation of those upper columns.  Its
changed support \(S\) is invariant under the permutation and has no fixed
point.  Thus it exists exactly when the nonloop inclusion graph on two
copies of \(S\) satisfies Hall.  No negative-association or probabilistic
claim is used.

The full-support corollary is also exact.  Every lower row is incident with
\(D={m+1\choose2}\) upper columns and every upper column contains \(D\)
lower rows.  Removing the source perfect matching leaves a balanced
\((D-1)\)-regular bipartite graph.  For \(m\ge2\), regular Hall supplies a
perfect matching with no source edge, so all old rows and all old collars
can be changed simultaneously at the palette level.  For \(m=1\), the
remaining degree is zero; this is the unique exception.  Cap two,
acyclicity and avoidance of newly created collars do not follow.

Every old short internal run has a collar of \(\ell+1\) source edges.
Leaving all of those diamonds unchanged leaves the literal bounded run, so
the changed support must hit every collar.  A source edge is charged by at
most the \(m+1\) coordinates in the union of its endpoints, proving the
stated transversal lower bound.  Hitting old collars does not prevent new
collars; the report states this.

The physical iff is also correct with its final-graph definition.  Under
maximum degree two and acyclicity, a selected forbidden collar is
consecutive in one path and is exactly one internally bounded positive run
of length below \(h\).  Conversely, every such run yields that selected
collar.  The family must be taken in the final Johnson lift and may cross
several inserted seams.  The report now says this explicitly.

## 3. Connector transducer and cut semantics

The literal connector criterion is tautological but exact:

* Johnson endpoint adjacency produces one spanning path;
* the fully concatenated coordinate words decide residence; and
* crossing windows need supply exactly the targets absent from all
  component interiors.

The proposed transducer retains sufficient and necessary information.
Coordinate traces use a finite run monoid with a distinct initial-boundary
state and an all-one/whole-fragment flag.  The last \(m\) middle masks
determine every new union and intersection window through the full flag
tower.  The labelled uncovered banks prevent independent rankwise choices.

The cut state is load-bearing.  Opening a cyclic \(11\) edge splits one run
into two exempt boundary arms; opening \(10\) or \(01\) exposes one arm;
opening \(00\) exposes none.  At depth \(q\), exactly \(q\) cyclic
\((q+1)\)-windows cross a fixed cut and disappear.  Thus a cyclic support
certificate alone does not prove the linear theorem.

The pairwise safe-port corollary is correctly restricted to components of
length at least \(h\).  Without this hypothesis it is false as a
composition rule: at \(h=3\),

\[
 (0,1)\mid(1)\mid(0)
\]

contains the forbidden trace \(0,1,1,0\), although neither seam viewed as an
isolated two-fragment replacement captures the full relayed run.  The exact
transducer handles this case.  The pairwise graph is therefore only a
sufficient face for the m5 local provider census.

## 4. Independent \(m=5\) replay

Three local audits were rerun.  Each used below 30 MB resident memory and
completed in approximately 0.04 seconds.

~~~text
python3 scratch/audit_catalan_m5_residence_rethread_c4c6_20260731.py
python3 scratch/audit_catalan_m5_residence_clean_socket_dead_component_h2_20260731.py
python3 scratch/audit_r_m5_residence_connector_local_census_20260731.py
~~~

They independently verify:

1. the exact two immediate palettes, 210 edges, 252 vertices, 42 path
   components, and no internal positive run below three;
2. 119 changed partners and alternating half-length histogram
   \(2^9 3^7 4^5 5^2 6^2 7^3 8^1 9^1\);
3. the 21 deeper debts listed in the theorem;
4. the lightweight \(84/304/293/608/114\) port and directed-arc census,
   including the four zero one-seam-provider debts; and
5. the stronger solver-free two-dead-socket theorem for the fixed path
   bodies.

The last theorem does not rely on pairwise sufficiency.  It exhibits two
literal forced defect collars at the two dead sockets.  They are
edge-disjoint for all connected neighbour choices; their unique overlap
choice isolates a two-component cycle.  A single linear opening cannot
remove both.  This closes endpoint-only joining of this one forest, not a
further interior rethread.

At \(h=3\), each coordinate has 42 unjoined runs and positive mass 126, so
the coordinatewise pressure is exactly zero.  The independently enumerated
deficit/excess pairs agree with the theorem.  This directly confirms that
zero scalar pressure is compatible with a dead socket distribution.

## 5. Controlled-debt and implication scope

Immediate-palette-neutral rethreads cannot be represented by a state whose
only progress coordinate is the set of immediate palette holes.  The
correct product state includes physical path pairing, the fully composed
run monoid, all-depth debt and the last owner tail, current decoration and
its transition debt, Pascal reachability, pairing-resolved occurrence linkage, and the
compiler/common-\(Q\) relation.  Empty-service arcs require an independent
finite acyclic stage or used-resource progress order.

This validates the state expansion in the companion turn-defect theorem.
It does not prove that the state has uniformly bounded adhesion or that
PBBS/Pascal supplies all required transitions.

The exact proved boundary is:

* all-\(m\): coordinate pressure, changed-support Hall, a full-support
  palette derangement for \(m\ge2\), the forbidden-collar characterization,
  and the literal connector transducer;
* \(m=5\): one central residence-clean forest and one fixed-socket no-go;
* open: a uniform q1-exact interior rethread with compatible sockets,
  all-depth connector service, accepted Pascal reachability, one exported
  terminal decoration for later transparent gluing, and the same-chronology
  common-\(Q\) compiler.

No claim of \(\nu(k)=B(k)\) for all \(k\), no K17 certificate, and no
bounded-size switch packet follows.
